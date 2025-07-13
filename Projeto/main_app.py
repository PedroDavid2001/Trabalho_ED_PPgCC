import tkinter as tk
from tkinter import ttk, messagebox
import random

from caracteristica import Caracteristicas
from participante import Participante
from evento import Evento


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
        self.bg_color = "#DCDAD5"       # Fundo levemente verde
        self.frame_bg = "#DCDAD5"       # Fundo dos frames

        master.configure(bg=self.bg_color)

        # Estilos ttk
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TFrame', background=self.frame_bg)
        style.configure('TLabelFrame', background=self.frame_bg, foreground='#333333', font=('Arial', 10, 'bold'))
        style.configure('TLabel', background=self.frame_bg, foreground='#333333', font=('Arial', 10))
        style.configure('TButton', background=self.primary_color, foreground=self.text_color, font=('Arial', 10, 'bold'), relief='flat')
        style.map('TButton', background=[('active', self.secondary_color)])
        style.configure('TEntry', fieldbackground='white', foreground='#333333')
        style.configure('TText', fieldbackground='white', foreground='#333333')

        self.participantes: list[Participante] = []
        self.dias_simulacao = int(0)
        self.dia_atual = int(0)

        # --- Frame de Configuração ---
        self.config_frame = ttk.LabelFrame(master, text="Configuração da Simulação")
        self.config_frame.pack(padx=15, pady=15, fill="x")

        ttk.Label(
            self.config_frame, text="Nomes dos Participantes (um por linha):").grid(
                row=0, column=0, padx=5, pady=5, sticky="nw")
        self.nomes_participantes_text = tk.Text(self.config_frame, height=8, width=30, wrap="word")
        self.nomes_participantes_text.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.nomes_participantes_text.insert(tk.END, "Alice\nRoberto\nCézar\nDiana\nEduardo\nPedro\nPaulo\nMaria\nMelissa\nAntonio\nCarlos\nAndré\nLuiza\nAndreza\nJulimar\nJoão\nLucas\nGian\nNeide\nLeandro")

        ttk.Label(
            self.config_frame, text="Duração (dias):").grid(
                row=1, column=0, padx=5, pady=5, sticky="w")
        self.duracao_dias_entry = ttk.Entry(self.config_frame, width=10)
        self.duracao_dias_entry.insert(0, "10")
        self.duracao_dias_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.iniciar_button = ttk.Button(
            self.config_frame, text="Iniciar Simulação", command=self.iniciar_simulacao)
        self.iniciar_button.grid(row=2, column=0, pady=10, padx=5, sticky="ew")

        self.passar_dia_button = ttk.Button(
            self.config_frame, text="Próximo Dia", command=self.simular_proximo_dia)
        self.passar_dia_button.grid(row=2, column=1, pady=10, padx=5, sticky="ew")
        self.passar_dia_button.config(state="disabled")
        
        # Configurar expansão de coluna para as entradas
        self.config_frame.grid_columnconfigure(1, weight=1)

        # --- Container para Status e Participantes (Coluna da Esquerda) ---
        self.left_column_frame = ttk.Frame(master, style='TFrame')
        self.left_column_frame.pack(side="left", padx=15, pady=10, fill="both", expand=True)

        # --- Frame de Status da Simulação ---
        self.status_frame = ttk.LabelFrame(self.left_column_frame, text="Status da Simulação")
        self.status_frame.pack(padx=0, pady=0, fill="x", anchor="n")

        self.dia_label = ttk.Label(self.status_frame, text="Dia: 0/0")
        self.dia_label.pack(padx=0, pady=0)

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

        self.log_text = tk.Text(
            self.log_frame, height=20, width=60, state="disabled", wrap="word")
        self.log_text.pack(padx=5, pady=5, fill="both", expand=True)
        self.log_text_scroll = ttk.Scrollbar(self.log_frame, command=self.log_text.yview)
        self.log_text_scroll.pack(side="right", fill="y")
        self.log_text.config(yscrollcommand=self.log_text_scroll.set)


    def log_evento(self, message: str, color="black"):
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
                char_names = [c.name for c in p.caracteristicas]
                self.participants_list_text.insert(tk.END,
                    f"- {p.nome}\n"
                    f"  Aptidão Física: {p.aptidao_fisica},\n"
                    f"  Raciocínio Lógico: {p.raciocinio_logico},\n"
                    f"  Humor: {p.humor}\n"
                    f"  Características: {', '.join(char_names)}\n\n"
                )
        self.participants_list_text.config(state="disabled")


    def iniciar_simulacao(self):
        """Inicia uma nova simulação do reality show."""
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

            # Reseta a lista de participantes se alguem tiver vencido na ultima simulação
            if len(self.participantes) <= 1:
                self.participantes = [Participante.gerar_participante(nome) for nome in nomes]

            self.log_evento(
                f"Iniciando simulação com {len(self.participantes)} participantes por {duracao} dias.",
                color=self.primary_color)
            
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

                self.log_evento(
                    f"- {p.nome} (Aptidão Física: {p.aptidao_fisica}, "
                    f"Raciocínio Lógico: {p.raciocinio_logico}, "
                    f"Humor: {p.humor})")
                self.log_evento(
                    f"  Caracteristicas: {', '.join(char_names)}")
                self.log_evento(
                    f"  Gosta: {', '.join(gosta_names) if gosta_names else 'Nenhum'}")
                self.log_evento(
                    f"  Detesta: {', '.join(detesta_names) if detesta_names else 'Nenhum'}\n")

            self.iniciar_button.config(state="disabled")
            self.passar_dia_button.config(state="normal")
            self.nomes_participantes_text.config(state="disabled")
            self.duracao_dias_entry.config(state="disabled")

        except ValueError:
            messagebox.showerror(
                "Erro de Entrada",
                "Por favor, insira um número válido para a duração.")

    def simular_proximo_dia(self):
        """Simula o próximo dia da casa, incluindo eventos e atualizações de status."""
        self.passar_dia_button.config(state="disabled")
        if self.dia_atual < self.dias_simulacao and len(self.participantes) > 1:
            self.dia_atual += 1
            self.dia_label.config(text=f"Dia: {self.dia_atual}/{self.dias_simulacao}")
            self.log_evento(
                f"\n--- Dia {self.dia_atual} ---", color=self.secondary_color)

            # Instancia um objeto Evento para o dia atual
            current_event = Evento("Evento do Dia", "Um evento aleatório acontece na casa.")

            # Eventos ocorrem aleatoriamente para maior dinamismo
            # Ajustei as probabilidades para o paredão ocorrer mais raramente
            event_type = random.choices(
                ["physical", "logical", "social", "voting", "nothing"],
                weights=[0.2, 0.2, 0.3, 0.1, 0.2], # 20% físico, 20% lógico, 30% social, 10% paredão, 20% nada
                k=1
            )[0]

            eliminado: Participante | None = None

            if event_type == "physical":
                self.log_evento(
                    f"--- Evento: Prova de Aptidão Física ---", color="red")
                self.log_evento(
                    f"Descrição: Teste de resistência física extremo!", color="red")
                self.participantes, eliminado = current_event.eliminar_participante(self.participantes, tipo_teste="fisico")

                if eliminado:
                    self.log_evento(
                        f"Participante eliminado por menor aptidão física:\n"
                        f"- {eliminado.nome} (Aptidão: {eliminado.aptidao_fisica})",
                        color="red")
                else:
                    self.log_evento(
                        "Ninguém foi eliminado nesta prova física.",
                        color="green")
            
            elif event_type == "logical":
                self.log_evento(
                    f"--- Evento: Prova de Raciocínio Lógico ---",
                    color="red")
                self.log_evento(
                    f"Descrição: Teste de conhecimentos gerais e raciocínio lógico!",
                    color="red")

                self.participantes, eliminado = current_event.eliminar_participante(self.participantes, tipo_teste="logico")
                if eliminado:
                    self.log_evento(
                        f"Participante eliminado por menor raciocínio lógico:\n"
                        f"- {eliminado.nome} (Raciocínio: {eliminado.raciocinio_logico})", color="red")
                else:
                    self.log_evento(
                        "Ninguém foi eliminado nesta prova de raciocínio.",
                        color="green")
            
            elif event_type == "social":
                self.log_evento(
                    "--- Evento: Interação Social na Casa! ---", color="blue")

                current_event.evento_social(self.participantes) # Chama o método da instância de Evento
                self.log_evento(
                    "O clima na casa mudou após interações sociais.", color="blue")
            
            elif event_type == "voting":
                self.log_evento("--- Será realizado o Paredão! ---", color="red")
                self.participantes, eliminado, maior_voto = current_event.paredao(self.participantes) # Chama o método da instância de Evento
                if eliminado:
                    self.log_evento(
                        f"Infelizmente {eliminado.nome} foi eliminado(a) com {maior_voto} votos.",
                        color="red")
                else:
                    self.log_evento(
                        "O paredão não resultou em eliminação.", color="orange")
                
            else:
                self.log_evento(
                    "Dia tranquilo na casa. Sem grandes eventos hoje.", color="gray")

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
                self.passar_dia_button.config(state="normal") # Habilita o botão para o próximo dia

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
            self.passar_dia_button.config(state="disabled") # Desabilita ao final da simulação


if __name__ == "__main__":
    root = tk.Tk()
    app = RealityShowApp(root)
    root.mainloop()