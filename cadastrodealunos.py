# Importa a biblioteca tkinter para criar a interface gráfica
import tkinter as tk
from tkinter import messagebox
import csv  # Importe a biblioteca 
from tkinter import ttk  # Importe ttk para usar os widgets estilizados

# Lista para armazenar informações dos alunos
ALUNOS = []


# Função para criar botões estilizados
def criar_botao_estilizado(parent, texto, comando):
    estilo = ttk.Style()
    estilo.configure("TButton", padding=10, relief="raised", font=("Arial", 12))
    botao = ttk.Button(parent, text=texto, command=comando, style="TButton")
    return botao

# Função que cria a tela principal com as opções do programa
def menu():
    # Cria um rótulo com o título
    label = tk.Label(root, text="CONTROLE DE TURMA", font=("Arial", 16))
    label.pack()

    # Cria um quadro para os botões
    buttons_frame = tk.Frame(root, bg="lightblue", relief="sunken", borderwidth=2)
    buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Cria botões para cada opção do programa
    btn_cadastro = criar_botao_estilizado(buttons_frame, "Cadastro de Aluno", cadastro_aluno)
    btn_cadastro.pack(pady=10)  # Adicione uma margem de 10 pixels na parte inferior do botão
    btn_edicao = criar_botao_estilizado(buttons_frame, "Edicao de Aluno", editar_aluno)
    btn_edicao.pack(pady=10)  # Adicione uma margem de 10 pixels na parte inferior do botão
    btn_exclusao = criar_botao_estilizado(buttons_frame, "Exclusao de Aluno", remover_aluno)
    btn_exclusao.pack(pady=10)  # Adicione uma margem de 10 pixels na parte inferior do botão
    btn_resumo = criar_botao_estilizado(buttons_frame, "Resumo Estatistico", resumo_estatistico)
    btn_resumo.pack(pady=10)  # Adicione uma margem de 10 pixels na parte inferior do botão
    btn_exportar = criar_botao_estilizado(buttons_frame, "Exportar Informacoes", exportar_arquivo)
    btn_exportar.pack(pady=10)  # Adicione uma margem de 10 pixels na parte inferior do botão
    btn_importar = criar_botao_estilizado(buttons_frame, "Importar Informacoes", importar_arquivo)
    btn_importar.pack(pady=10)  # Adicione uma margem de 10 pixels na parte inferior do botão

    # Exibe os botões na tela
    btn_cadastro.pack()
    btn_edicao.pack()
    btn_exclusao.pack()
    btn_resumo.pack()
    btn_exportar.pack()
    btn_importar.pack()

# Função para cadastrar um novo aluno
def cadastro_aluno():
    # Cria uma nova janela para o cadastro de aluno
    def cadastrar():
        ra = int(entry_ra.get())
        nome = entry_nome.get()
        nota = float(entry_nota.get())

        aluno = {
            "ra": ra,
            "nome": nome,
            "nota": nota,
        }
        ALUNOS.append(aluno)
        messagebox.showinfo("Cadastro de Aluno", "Aluno cadastrado com sucesso!")
        top.destroy()

    # Cria a janela de cadastro
    top = tk.Toplevel(root)
    top.title("Cadastro de Aluno")

    # Cria campos de entrada para RA, nome e nota
    tk.Label(top, text="RA:").pack()
    entry_ra = tk.Entry(top)
    entry_ra.pack()

    tk.Label(top, text="Nome:").pack()
    entry_nome = tk.Entry(top)
    entry_nome.pack()

    tk.Label(top, text="Nota:").pack()
    entry_nota = tk.Entry(top)
    entry_nota.pack()

    # Cria um botão para cadastrar o aluno
    btn_cadastrar = tk.Button(top, text="Cadastrar", command=cadastrar)
    btn_cadastrar.pack()

# Função para editar os dados de um aluno
def editar_aluno():
    # Cria uma nova janela para a edição de aluno
    def salvar_edicao():
        ra = int(entry_ra.get())
        novo_nome = entry_nome.get()
        nova_nota = float(entry_nota.get())

        for aluno in ALUNOS:
            if aluno["ra"] == ra:
                aluno["nome"] = novo_nome
                aluno["nota"] = nova_nota
                messagebox.showinfo("Edicao de Aluno", "Aluno editado com sucesso!")
                top.destroy()
                return

        messagebox.showerror("Edicao de Aluno", "RA nao encontrado!")

    # Cria a janela de edição
    top = tk.Toplevel(root)
    top.title("Edicao de Aluno")

    # Cria campos de entrada para RA, novo nome e nova nota
    tk.Label(top, text="RA:").pack()
    entry_ra = tk.Entry(top)
    entry_ra.pack()

    tk.Label(top, text="Novo Nome:").pack()
    entry_nome = tk.Entry(top)
    entry_nome.pack()

    tk.Label(top, text="Nova Nota:").pack()
    entry_nota = tk.Entry(top)
    entry_nota.pack()

    # Cria um botão para salvar a edição
    btn_salvar = tk.Button(top, text="Salvar Edicao", command=salvar_edicao)
    btn_salvar.pack()

# Função para remover um aluno
def remover_aluno():
    # Cria uma nova janela para a exclusão de aluno
    def remover():
        ra = int(entry_ra.get())
        for aluno in ALUNOS:
            if aluno["ra"] == ra:
                ALUNOS.remove(aluno)
                messagebox.showinfo("Exclusao de Aluno", "Aluno removido com sucesso!")
                top.destroy()
                return

        messagebox.showerror("Exclusao de Aluno", "RA nao encontrado!")

    # Cria a janela de exclusão
    top = tk.Toplevel(root)
    top.title("Exclusao de Aluno")

    # Cria um campo de entrada para o RA
    tk.Label(top, text="RA:").pack()
    entry_ra = tk.Entry(top)
    entry_ra.pack()

    # Cria um botão para remover o aluno
    btn_remover = tk.Button(top, text="Remover Aluno", command=remover)
    btn_remover.pack()

# Função para exibir um resumo estatístico da turma
def resumo_estatistico():
    quantidade_alunos = len(ALUNOS)

    if quantidade_alunos == 0:
        messagebox.showinfo("Resumo Estatistico", "Nao existem alunos cadastrados")
    else:
        aluno_menor, aluno_maior = get_aluno_menor_maior_nota()

        notas = [aluno["nota"] for aluno in ALUNOS]
        media_notas = sum(notas) / quantidade_alunos

        mensagem = f"Resumo Estatistico da Turma:\n"
        mensagem += f"Quantidade de Alunos: {quantidade_alunos}\n"
        mensagem += f"Maior Nota: {aluno_maior['nome']} - Nota: {aluno_maior['nota']}\n"
        mensagem += f"Menor Nota: {aluno_menor['nome']} - Nota: {aluno_menor['nota']}\n"
        mensagem += f"Media das Notas da Turma: {media_notas:.2f}"

        messagebox.showinfo("Resumo Estatistico", mensagem)

# Função para obter o aluno com a menor e a maior nota
def get_aluno_menor_maior_nota():
    menor_atual = 1000
    maior_atual = -1000

    aluno_menor_nota = None
    aluno_maior_nota = None

    for aluno in ALUNOS:
        if aluno["nota"] < menor_atual:
            menor_atual = aluno["nota"]
            aluno_menor_nota = aluno

        if aluno["nota"] > maior_atual:
            maior_atual = aluno["nota"]
            aluno_maior_nota = aluno

    return aluno_menor_nota, aluno_maior_nota

# Função para exportar informações para um arquivo CSV
def exportar_arquivo():
    def exportar():
        nome_arquivo = entry_exportar_arquivo.get()  # Obtém o nome do arquivo a ser exportado
        if not nome_arquivo:
            messagebox.showerror("Exportar Informacoes", "Digite o nome do arquivo")
            return

        try:
            with open(nome_arquivo, "w", newline="") as arquivo_csv:
                # Crie um objeto escritor CSV
                csv_writer = csv.writer(arquivo_csv, delimiter="|")

                # Escreva os cabeçalhos
                csv_writer.writerow(["RA", "Nome", "Nota"])

                # Escreva os dados dos alunos
                for aluno in ALUNOS:
                    csv_writer.writerow([aluno["ra"], aluno["nome"], aluno["nota"]])

            messagebox.showinfo("Exportar Informacoes", "Informacoes exportadas com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro ao Exportar Informacoes", str(e))

    # Cria a janela de exportação
    top = tk.Toplevel(root)
    top.title("Exportar Informacoes")

    # Cria um campo de entrada para o nome do arquivo de exportação
    tk.Label(top, text="Nome do Arquivo:").pack()
    entry_exportar_arquivo = tk.Entry(top)
    entry_exportar_arquivo.pack()

    # Cria um botão para realizar a exportação
    btn_exportar = tk.Button(top, text="Exportar", command=exportar)
    btn_exportar.pack()

# Função para importar informações de um arquivo CSV
def importar_arquivo():
    def importar():
        nome_arquivo = entry_importar_arquivo.get()  # Obtém o nome do arquivo a ser importado
        if not nome_arquivo:
            messagebox.showerror("Importar Informacoes", "Digite o nome do arquivo")
            return

        try:
            with open(nome_arquivo, "r") as arquivo_csv:
                # Crie um leitor CSV
                csv_reader = csv.reader(arquivo_csv, delimiter="|")

                # Pule a linha de cabeçalho
                next(csv_reader)

                # Limpe a lista de ALUNOS antes de importar
                ALUNOS.clear()

                # Importe os dados dos alunos
                for linha in csv_reader:
                    ra, nome, nota = linha
                    aluno = {
                        "ra": int(ra),
                        "nome": nome,
                        "nota": float(nota),
                    }
                    ALUNOS.append(aluno)

            messagebox.showinfo("Importar Informacoes", "Informacoes importadas com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro ao Importar Informacoes", str(e))

    # Cria a janela de importação
    top = tk.Toplevel(root)
    top.title("Importar Informacoes")

    # Cria um campo de entrada para o nome do arquivo de importação
    tk.Label(top, text="Nome do Arquivo:").pack()
    entry_importar_arquivo = tk.Entry(top)
    entry_importar_arquivo.pack()

    # Cria um botão para realizar a importação
    btn_importar = tk.Button(top, text="Importar", command=importar)
    btn_importar.pack()

# Cria a janela principal
root = tk.Tk()
root.configure(bg="lightblue")  # Cor de fundo da janela principal
root.geometry("800x600")  # Tamanho da janela
root.title("Controle de Turma")
menu()  # Chama a função menu para exibir a tela principal
root.mainloop()

