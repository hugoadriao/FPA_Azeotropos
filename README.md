# FPA_Azeotropos <h1>
Este trabalho contém o código do Algoritmo de Polinização das Flores (APF) e do Cálculo de Azeótropos Homogêneos não Reativos de Misturas Binárias.
Para a utilização em trabalhos:
	Este projeto está livre para a utilização em trabalhos, lembre-se apenas de referencia-lo.

#### Descrição Geral:<h4>
Antes de mais nada abra o arquivo “gera_teste.py”, este arquivo contém o padrão utilizado na criação das populações que também é o nome que deve ser dado aos arquivos txt que irão conter estas populações, ou seja, quando for perguntado “nome do arquivo” utilize um dos padrões listados.
	Exemplo:
		```
	“gerar nova população?”
		```
		```
	s
		```
		```
	“nome do arquivo”
		```
		```
	AC
		```
	<p>O algoritmo irá interpretar que a mistura problema é acetona-clorofórmio a 1Atm.</p>
	<p>Para início do software execute o arquivo “principal.py”.</p>
	<p>As pastas “populacao” e “result” contém, respectivamente, populações criadas para todas as misturas e resultados para todas as misturas.</p>
	<p>Caso seja de interesse realizar um teste com populações existentes:</p>
	<p>Execute o arquivo “principal.py”</p>
		```
	“gerar nova população?”
		```
		```
	n
		```
		```
	“nome do arquivo”
		```
		```
	AC
		```
		```
	“nome do arquivo de resultados”
		```
		```
	qualquer_coisa
		```
	<p>Seguindo os passos descritos anteriormente será salvo um resultado no arquivo “qualquer_coisa.txt” na pasta “result” para a população salva na pasta “populacao” no arquivo “AC.txt”.</p>
	<p>As saídas nos arquivos resultado são:</p>
	<p>Número de vezes que o método APF foi executado; número de avaliações da função objetivo; {temperatura: Kelvin, frac_1: fração molar do primeiro componente, frac_2: fração molar do segundo componente}; resultado da função objetivo.</p>
	<p>Os dados utilizados podem ser encontrados em:</p>
<p><b>Yang, X.S. Nature-inspired algorithms and applied optimization; Vol. 744, Springer, 2017.</b></p>
<p><b>Maier, R.W.; Brennecke, J.F.; Stadtherr, M.A. Reliable computation of homogeneous azeotropes. AIChE Journal 1998, 44, 1745-1755.</b></p>
<p><b>Azevedo,  M.M.G.O.d.;  others. ANÁLISE DO DESEMPENHO  DE  MÉTODOS  DE INTELIGÊNCIA  ARTIFICIAL  BASEADOS  NO  COMPORTAMENTO  DAS  PLANTAS 2017.</b></p>
