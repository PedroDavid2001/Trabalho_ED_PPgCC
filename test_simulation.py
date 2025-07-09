from participante import gerar_participante
from evento import Evento

print("--- Inicializando Participantes ---")

# Criando alguns participantes de exemplo usando a função gerar_participante
participante1 = gerar_participante("Alice")
participante2 = gerar_participante("Bob")
participante3 = gerar_participante("Charlie")
participante4 = gerar_participante("Diana")
participante5 = gerar_participante("Eduardo")


participantes_atuais = [
    participante1,
    participante2,
    participante3,
    participante4,
    participante5,
]

print("\nParticipantes antes do evento:")
for p in participantes_atuais:
    print(f"- Nome: {p.nome}")
    print(f"  Aptidão Física: {p.aptidao_fisica}")
    print(f"  Humor: {p.humor}")
    print(f"  Características: {[c.name for c in p.caracteristicas]}")
    print(f"  Gosta de: {[c.name for c in p.gosta]}")
    print(f"  Detesta: {[c.name for c in p.detesta]}")
    print("-" * 20)


# Criando um evento de resistência
evento_resistencia = Evento(
    "Desafio da Superação",
    "Os participantes precisam provar sua resistência em um teste árduo para permanecer na casa.",
)

# Executando o evento e obtendo a nova lista de participantes
participantes_apos_evento = evento_resistencia.eliminar_por_aptidao_fisica(
    participantes_atuais
)

print("\n--- Participantes após o evento ---")
if participantes_apos_evento:
    for p in participantes_apos_evento:
        print(f"- {p.nome} (Aptidão: {p.aptidao_fisica}, Humor: {p.humor})")
else:
    print(
        "Todos os participantes foram eliminados ou não havia participantes restantes."
    )
