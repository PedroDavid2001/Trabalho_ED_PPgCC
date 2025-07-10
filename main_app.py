import tkinter as tk
from tkinter import ttk, messagebox
import random

from caracteristica import Caracteristicas
from participante import gerar_participante, Participante
from evento import Evento
from relacoes import MatrizRelacoes


class RealityShowApp:
    def __init__(self, master: tk.Tk):
        self.master = master
        master.title("Simulador de Reality Show")
        master.geometry("900x700")
        master.resizable(True, True)

        # Cores para a interface
        self.primary_color = "#30A534"  # Verde vibrante
        self.secondary_color = "#33B633" # Verde claro
        self.accent_color = "#FFC107"   # Amarelo para destaque
        self.text_color = "#FFFFFF"     # Texto branco
        self.bg_color = "#FFFFFF"       # Fundo levemente verde
        self.frame_bg = "#FFFFFF"       # Fundo dos frames

        master.configure(bg=self.bg_color)

        # Estilos ttk
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            'TFrame')
        style.configure(
            'TLabelFrame', font=('Arial', 10, 'bold'))
        style.configure(
            'TLabel', font=('Arial', 10))
        style.configure(
            'TButton', background=self.primary_color, foreground=self.text_color, font=('Arial', 10, 'bold'), relief='flat')
        style.map(
            'TButton', background=[('active', self.secondary_color)])
        style.configure(
            'TEntry', fieldbackground='white', foreground='#333333')
        style.configure(
            'TText', fieldbackground='white', foreground='#333333')

        self.participantes: list[Participante] = []
        self.dias_simulacao = int(0)
        self.dia_atual = int(0)

        # --- Frame de Configuração (continua usando pack na parte superior) ---
        self.config_frame = ttk.LabelFrame(master, text="Configuração da Simulação")
        self.config_frame.pack(padx=15, pady=15, fill="x")

        ttk.Label(
            self.config_frame, text="Nomes dos Participantes (um por linha):").grid(
                row=0, column=0, padx=5, pady=5, sticky="nw")
        self.nomes_participantes_text = tk.Text(self.config_frame, height=8, width=30, wrap="word")
        self.nomes_participantes_text.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.nomes_participantes_text.insert(tk.END, "Alice\nBob\nCharlie\nDiana\nEduardo")

        ttk.Label(
            self.config_frame, text="Duração (dias):").grid(
                row=1, column=0, padx=5, pady=5, sticky="w")
        self.duracao_dias_entry = ttk.Entry(self.config_frame, width=10)
        self.duracao_dias_entry.insert(0, "10")
        self.duracao_dias_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.iniciar_button = ttk.Button(
            self.config_frame, text="Iniciar Simulação", command=self.iniciar_simulacao)
        self.iniciar_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Configurar expansão de coluna para as entradas
        self.config_frame.grid_columnconfigure(1, weight=1)

        # --- Container para Status e Participantes (Coluna da Esquerda) ---
        self.left_column_frame = ttk.Frame(master, style='TFrame')
        self.left_column_frame.pack(side="left", padx=15, pady=10, fill="both", expand=True)

        # --- Frame de Status da Simulação ---
        self.status_frame = ttk.LabelFrame(self.left_column_frame, text="Status da Simulação")
        self.status_frame.pack(padx=0, pady=0, fill="x", anchor="n")

        self.dia_label = ttk.Label(self.status_frame, text="Dia: 0/0")
        self.dia_label.pack(pady=5)

        self.participantes_label = ttk.Label(self.status_frame, text="Participantes Atuais: 0")
        self.participantes_label.pack(pady=5)

        # --- Frame de Participantes Atuais ---
        self.current_participants_frame = ttk.LabelFrame(
            self.left_column_frame, text="Participantes na Casa")
        self.current_participants_frame.pack(padx=0, pady=10, fill="both", expand=True)

        self.participants_list_text = tk.Text(
            self.current_participants_frame, height=5, width=40, state="disabled", wrap="word")
        self.participants_list_text.pack(padx=5, pady=5, fill="both", expand=True)
        self.participants_list_scroll = ttk.Scrollbar(
            self.current_participants_frame, command=self.participants_list_text.yview)
        self.participants_list_scroll.pack(side="right", fill="y")
        self.participants_list_text.config(yscrollcommand=self.participants_list_scroll.set)

        # --- Área de Log/Eventos (Coluna da Direita) ---
        self.log_frame = ttk.LabelFrame(master, text="Log de Eventos")
        self.log_frame.pack(side="right", padx=15, pady=10, fill="both", expand=True)

        self.log_text = tk.Text(self.log_frame, height=20, width=60, state="disabled", wrap="word")
        self.log_text.pack(padx=5, pady=5, fill="both", expand=True)
        self.log_text_scroll = ttk.Scrollbar(self.log_frame, command=self.log_text.yview)
        self.log_text_scroll.pack(side="right", fill="y")
        self.log_text.config(yscrollcommand=self.log_text_scroll.set)


    def log_evento(self, message, color="black"):
        """Adiciona uma mensagem ao log de eventos na interface com uma cor opcional."""
        self.log_text.config(state="normal")
        self.log_text.tag_configure("color", foreground=color)
        self.log_text.insert(tk.END, message + "\n", "color")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")


    def update_participants_list(self):
        """Atualiza a lista de participantes visível na interface."""
        self.participants_list_text.config(state="normal")
        self.participants_list_text.delete(1.0, tk.END)
        if not self.participantes:
            self.participants_list_text.insert(tk.END, "Nenhum participante na casa.")
        else:
            for p in self.participantes:
                # Mostrar as características também, para uma visão mais completa
                char_names = [c.name for c in p.caracteristicas]
                self.participants_list_text.insert(tk.END,
                    f"- {p.nome}\n"
                    f"  Aptidão: {p.aptidao_fisica}, Humor: {p.humor}\n"
                    f"  Características: {', '.join(char_names)}\n\n"
                )
        self.participants_list_text.config(state="disabled")


    def iniciar_simulacao(self):
        nomes_str = self.nomes_participantes_text.get(1.0, tk.END).strip()
        if not nomes_str:
            messagebox.showerror(
                "Erro de Entrada",
                "Por favor, insira os nomes dos participantes.")
            return

        nomes = [nome.strip() for nome in nomes_str.split('\n') if nome.strip()]
        if not nomes:
            messagebox.showerror(
                "Erro de Entrada",
                "Nenhum nome de participante válido encontrado.")
            return

        try:
            duracao = int(self.duracao_dias_entry.get())
            if duracao <= 0:
                messagebox.showerror(
                    "Erro de Entrada",
                    "A duração da simulação deve ser maior que zero.")
                return

            self.log_text.config(state="normal")
            self.log_text.delete(1.0, tk.END)
            self.log_text.config(state="disabled")

            self.log_evento(
                f"Iniciando simulação com {len(nomes)} participantes por {duracao} dias.",
                color=self.primary_color)
            self.participantes = [gerar_participante(nome) for nome in nomes]
            self.dias_simulacao = duracao
            self.dia_atual = 0

            self.dia_label.config(text=f"Dia: {self.dia_atual}/{self.dias_simulacao}")
            self.participantes_label.config(text=f"Participantes Atuais: {len(self.participantes)}")
            self.update_participants_list()
            self.log_evento("Participantes gerados:")

            for p in self.participantes:
                char_names = [c.name for c in p.caracteristicas]
                gosta_names = [c.name for c in p.gosta]
                detesta_names = [c.name for c in p.detesta]

                self.log_evento(f"- {p.nome} (Apt: {p.aptidao_fisica}, Humor: {p.humor})")
                self.log_evento(f"  Caracteristicas: {', '.join(char_names)}")
                self.log_evento(f"  Gosta: {', '.join(gosta_names) if gosta_names else 'Nenhum'}")
                self.log_evento(f"  Detesta: {', '.join(detesta_names) if detesta_names else 'Nenhum'}\n")

            self.iniciar_button.config(state="disabled")
            self.nomes_participantes_text.config(state="disabled")
            self.duracao_dias_entry.config(state="disabled")

            self.master.after(700, self.simular_proximo_dia)

        except ValueError:
            messagebox.showerror(
                "Erro de Entrada",
                "Por favor, insira um número válido para a duração.")


    def simular_proximo_dia(self):
        if self.dia_atual < self.dias_simulacao and len(self.participantes) > 1:
            self.dia_atual += 1
            self.dia_label.config(text=f"Dia: {self.dia_atual}/{self.dias_simulacao}")
            self.log_evento(f"\n--- Dia {self.dia_atual} ---", color=self.secondary_color)

            # Eventos ocorrem aleatoriamente para maior dinamismo
            event_type = random.choice(["physical", "social", "nothing"])

            if event_type == "physical" and self.dia_atual >= 1: # Evento físico pode ocorrer a partir do dia 1
                self.log_evento(
                    "Evento: Prova de Aptidão Física!", color="red")

                evento_fisico = Evento("Prova de Aptidão Física", "Teste de resistência física extremo!")
                num_antes = len(self.participantes)
                self.participantes = evento_fisico.eliminar_por_aptidao_fisica(self.participantes)

                if len(self.participantes) < num_antes:
                    self.log_evento(
                        "Um participante foi eliminado na prova física.",
                        color="red")
                else:
                    self.log_evento(
                        "Ninguém foi eliminado nesta prova física (pode ocorrer se aptidão for igual).",
                        color="green")
            
            elif event_type == "social" and self.dia_atual >= 1: # Evento social pode ocorrer a partir do dia 1
                self.log_evento(
                    "Evento: Interação Social na Casa!", color="blue")
                self.evento_social()
            else:
                self.log_evento(
                    "Dia tranquilo na casa. Sem grandes eventos hoje.", color="gray")

            # TODO: Adicionar o evento de paredão aqui quando a lógica estiver pronta.

            self.participantes_label.config(
                text=f"Participantes Atuais: {len(self.participantes)}")
            self.update_participants_list()

            if len(self.participantes) == 0:
                self.log_evento(
                    "\nFim da simulação: Todos os participantes foram eliminados!", color="red")

            elif len(self.participantes) == 1:
                self.log_evento(
                    f"\nFim da simulação: O vencedor é {self.participantes[0].nome}!", color="green")

            else:
                self.master.after(1000, self.simular_proximo_dia)

        else:
            self.log_evento("\nSimulação Concluída.", color=self.primary_color)
            if len(self.participantes) > 0:
                self.log_evento(
                    f"Participantes restantes: {[p.nome for p in self.participantes]}", color="green")
            else:
                self.log_evento(
                    "Todos os participantes foram eliminados.", color="red")

            self.iniciar_button.config(state="normal")
            self.nomes_participantes_text.config(state="normal")
            self.duracao_dias_entry.config(state="normal")


    def evento_social(self):
        """Simula um evento social que pode mudar o humor dos participantes."""
        from caracteristica import Caracteristicas
        from humor import Humor

        if not self.participantes:
            return

        # Para tornar o evento social mais interessante, vamos focar em dois participantes
        if len(self.participantes) < 2:
            self.log_evento(
                "Não há participantes suficientes para um evento social complexo.",
                color="orange"
            )
            return

        p1, p2 = random.sample(self.participantes, 2)
        
        self.log_evento(f"Houve uma interação social entre {p1.nome} e {p2.nome}.", color="blue")

        # Exemplo de interação: se um é tagarela e o outro tímido, o tímido pode ficar irritado ou triste
        if Caracteristicas.TAGARELA in p1.caracteristicas and Caracteristicas.TIMIDO in p2.caracteristicas:
            p2.humor_atual(Humor.IRRITADO)
            self.log_evento(
                f"- {p2.nome} (tímido) ficou IRRITADO com a tagarelice de {p1.nome}.", color="purple")

        elif Caracteristicas.AMIGAVEL in p1.caracteristicas and p2.humor == Humor.TRISTE:
            p2.humor_atual(Humor.NEUTRO)
            self.log_evento(
                f"- {p1.nome} (amigável) ajudou {p2.nome} a se sentir NEUTRO novamente.", color="green")

        else:
            # Caso geral: humor aleatório para alguns
            for p in random.sample(self.participantes, k=min(len(self.participantes), 3)): # Afeta até 3 participantes
                old_humor = p.humor
                possible_humors = [Humor.ALEGRE, Humor.IRRITADO, Humor.CANSADO, Humor.TRISTE, Humor.NEUTRO]
                new_humor = random.choice([h for h in possible_humors if h != old_humor])
                p.humor_atual(new_humor)
                self.log_evento(
                    f"- O humor de {p.nome} mudou de {old_humor} para {new_humor}.", color="darkblue")


if __name__ == "__main__":
    root = tk.Tk()
    app = RealityShowApp(root)
    root.mainloop()