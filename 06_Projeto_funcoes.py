# Aula 06 - Projeto Funções

# Escreva um programa para cadastro de livros com as seguints informações:
# Cadastrar
# Editar
# Remover
# Buscar por código
# Buscar todos
# Emprestar
# Devolver

'''
{
- codigo
- titulo
- autor
- categoria
- emprestado
}

'''

# Variável global para gerar códigos únicos para os livros.
banco = [
    {
        'codigo': 1,
        'titulo': 'Código limpo',
        'autor': 'Roberth',
        'categoria': 'Programação',
        'alugado': False,
        'preco': 15.90 
    }
]
codigo_atual = 1 # Variável global

def add_livro(titulo: str, autor: str, categoria: str, preco: float):
    global codigo_atual # Destravar a variável global
    codigo_atual += 1
    livro = {
        'codigo': codigo_atual,
        'titulo': titulo,
        'autor': autor,
        'categoria': categoria,
        'alugado': False,
        'preco': preco
    }
    banco.append(livro)
    print('Livro cadastrado com sucesso!')

def input_add_livro():
    titulo = input('Título: ')
    autor = input('Autor: ')
    categoria = input('Categoria: ')
    preco = float(input('Preço: '))
    add_livro(titulo, autor, categoria, preco)

def buscar_por_codigo(codigo:int):
    for livro in banco:
        if livro['codigo'] == codigo:
            return livro
    return None

def input_buscar_por_codigo():
    codigo = int(input('Codigo: '))
    livro = buscar_por_codigo(codigo)
    if livro:
        print('--- DADOS DO LIVRO ---')
        print(f'Código: {livro["codigo"]}')
        print(f'Título: {livro["titulo"]}')
        print(f'Autor: {livro["autor"]}')
        print(f'Categoria: {livro["categoria"]}')
        print(f'Preço: {livro["preco"]}')
        print(f'Alugado: {livro["alugado"]}')
        return
    print('Livro não encontrado!')

def editar_livro(codigo: int, titulo:int, autor:str, categoria:str, preco:float):
    livro = buscar_por_codigo(codigo)
    if livro:
        livro['titulo'] = titulo
        livro['autor'] = autor
        livro['categoria'] = categoria
        livro['preco'] = preco
        print('Livro editado com sucesso!')
    else:
        print('Livro não encontrado!')

def input_edit_livro():
    codigo = int(input('Código: '))
    if buscar_por_codigo(codigo):
        titulo = input('Título: ')
        autor = input('Autor: ')
        categoria = input('Categoria: ')
        preco = float(input('Preço: '))
        editar_livro(codigo, titulo, autor, categoria, preco)
    else:
        print('Livro não encontrado!')

def delete_livro(codigo:int):
    livro = buscar_por_codigo(codigo)
    banco.remove(livro)
    print('Livro excluído com sucesso!')

def input_delete_livro():
    codigo = int(input('Código: '))
    livro = buscar_por_codigo(codigo)
    if livro:
        delete_livro(codigo)
    else:
        print('Livro não encontrado!')

def listar_todos():
    for livro in banco:
        print('--- DADOS DO LIVRO ---')
        print(f'Código: {livro["codigo"]}')
        print(f'Título: {livro["titulo"]}')
        print(f'Autor: {livro["autor"]}')
        print(f'Categoria: {livro["categoria"]}')
        print(f'Preço: {livro["preco"]}')
        print(f'Alugado: {livro["alugado"]}')
        print('-'*50)

def alugar_livro(codigo:int):
    livro = buscar_por_codigo(codigo)
    if livro:
        if livro['alugado']:
            livro['alugado'] = False
            print('Livro já está alugado!')
        else:
            print('Livro alugado com sucesso!') 

def input_alugar_livro():
    codigo = int(input('Código: '))
    livro = buscar_por_codigo(codigo)
    if livro:
        alugar_livro(codigo)
    else:
        print('Livro não encontrado!')  

def devolver_livro(codigo:int):
    livro = buscar_por_codigo(codigo)
    if livro:
        print('Livro devolvido com sucesso')
        return
    print('Livro não encontrado!')

def input_devolver_livro():
    codigo = int(input('Código: '))
    livro = buscar_por_codigo(codigo)
    if livro:
        devolver_livro(codigo)
    else:
        print('Livro não encontrado!')

def menu():
    while True:
        print('--- BEM VINDO AO MENU ---')
        print('1 - Cadastrar livro')
        print('2 - Editar livro')
        print('3 - Buscar livro')
        print('4 - Remover livro')
        print('5 - Listar todos')
        print('6 - Alugar livro')
        print('7 - Devolver livro')
        print('8 - Sair')

        opcao = input('Selecione uma opção: ')
        if opcao == '1':
            input_add_livro()
        elif opcao == '2':
            input_edit_livro()
        elif opcao == '3':
            input_buscar_por_codigo()
        elif opcao == '4':
            input_delete_livro()
        elif opcao == '5':
            listar_todos()
        elif opcao == '6':
            input_alugar_livro()
        elif opcao == '7':
            input_devolver_livro()
        elif opcao == '8':
            print('Você saiu do programa!')
            break
        
menu() 