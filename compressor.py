import string

try:
    with open('/Users/joao/Documents/ProjetoCompressor/Teste.txt', 'r') as arquivo:
        texto = arquivo.read()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
except Exception as e:
    print("Ocorreu um erro ao abrir o arquivo:", e)

# Utilize o alfabeto completo para garantir que todos os caracteres sejam considerados
alfabeto = string.ascii_letters + string.digits + string.punctuation + " "

# Contador de caractere
def contarCaractere(texto):
    #primeiro cria-se um dicionário
    frequencia = {}
    for char in texto:
        if char in frequencia:
            frequencia[char] += 1
        else:
            frequencia[char] = 1 
    return frequencia
    
def gerar_codigo_de_compactacao(frequencia):
    codigo_compactacao = {}
    codigo = 0
    for char in sorted(frequencia, key=frequencia.get, reverse=True):
        codigo_compactacao[char] = bin(codigo)[2:]
        codigo += 1
    return codigo_compactacao

def compactarArquivo(codigoCompactacao, texto):
    textoCompactado = ""
    for char in texto:
        if char in codigoCompactacao:
            textoCompactado += codigoCompactacao[char]
        else:
            # Caso o caractere não esteja na lista
            textoCompactado += char
    return textoCompactado
