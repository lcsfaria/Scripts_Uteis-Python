# spacetotab.py

Troca os espaços em branco por tab

Quando copiamos algumsa informaçoes através do CTRL+C pode ocorrer que os Tab (\t) sejam substituidos por espaços em branco.
Para evitar isso, o scripit lê linha a linha, faz um split por qualquer tamanho de espaço (um espaço entre os valores, dois espaços entre os valores, ...) e retorna um arquivo separado por tab.

É necessário ter a biblioteca pandas previamente instalada.

# merge_with_intersection.py

Cria um arquivo novo baseado na interseçao de outros dois. Ordena pelo Index padrao gerado pelo pandas e a interseção pela(s) coluna(s) que desejamos.


É necessário ter a biblioteca pandas previamente instalada.

# mean_columns.py

Tome um data frame onde o index são os **'ID dos individuos'** e **'Pop'** a População a qual cada individuo pertence. Para de saber média de cada População, agrupamos os individuos da mesma População e calculamos a média das colunas desejadas.

É necessário ter a biblioteca pandas previamente instalada.
