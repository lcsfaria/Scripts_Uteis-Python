# SpaceToTab

Troca os espaços em branco por tab

Quando copiamos algumsa informaçoes através do CTRL+C pode ocorrer que os Tab (\t) sejam substituidos por espaços em branco.
Para evitar isso, o scripit lê linha a linha, faz um split por qualquer tamanho de espaço (um espaço entre os valores, dois espaços entre os valores, ...) e retorna um arquivo separado por tab.

É necessário ter a biblioteca pandas previamente instalada.

# Merge with intersection

Cria um arquivo novo baseado na interseçao de outros dois. Ordena pelo Index padrao gerado pelo pandas.
