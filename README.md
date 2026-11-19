1.2

a) Mudou só pra incluir os campos novos (páginas, isbn e capa). As regras ficam no model, e o ModelForm monta os campos a partir dele levando os validators junto. No is_valid() ele ainda chama o full_clean() do model. O Admin também é um ModelForm em cima do model, então pega as mesmas regras sem mexer em nada.

b) O validator é uma função que recebe só o valor e aprova ou recusa, e vale em qualquer lugar que use o model. O clean_<campo>() é do form, enxerga o resto do form e pode devolver o valor alterado. Exemplo que só dá com clean_<campo>(): tirar os espaços sobrando do título, porque o validator não muda o valor.

c) Título diferente do nome do autor: clean(), porque compara dois campos.
Título sem espaços no início e no fim: clean_title(), porque precisa alterar o valor antes de salvar.
Máximo de 5000 páginas: validators=[MaxValueValidator(5000)], é regra de um campo só e o Django já tem pronta.
Livro indisponível precisa de ISBN: clean(), porque depende de available e isbn juntos. Coloquei no clean() do model pra valer no Admin também.

2.2

a) Sem o request.FILES na view o livro salva normal, mas a capa fica vazia, porque o form nunca recebe o arquivo. Sem o enctype no template acontece a mesma coisa, o navegador manda só o nome do arquivo e o request.FILES chega vazio. Nos dois casos o formulário não deu aviso nenhum, já que a capa é opcional.

b) O static é pros arquivos do próprio projeto, tipo CSS e imagens do site, que são iguais pra todo mundo. O media é pro que o usuário envia, e o banco guarda só o caminho. Aqui o CSS seria static e as capas são media, usando livro.capa.url.

c) Porque o Django apaga só o registro no banco, não o arquivo. Com o tempo a pasta enche de imagem que ninguém usa, ocupando espaço e deixando o backup maior.

d) Porque dá pra renomear qualquer arquivo pra .png. O servidor tem que conferir se é imagem mesmo (o ImageField faz isso com o Pillow), limitar o tamanho, trocar o nome do arquivo e não deixar executar nada na pasta de uploads.

3.1

a) A própria CreateView. No GET ela mostra o form vazio e no POST valida e chama form_valid() ou form_invalid(). Se for inválido, mostra o mesmo template com os erros e o que a pessoa já tinha digitado, sem salvar.

b) Porque a CreateView já passa request.POST e request.FILES pro form sozinha.

c) Pra pessoa poder desistir, e porque excluir muda dados, então tem que ser POST com CSRF. Se fosse no GET, qualquer link aberto sem querer, ou um robô de busca passando pela página, apagaria o livro.

d) Vantagem: bem menos código, porque o CRUD já vem pronto. Desvantagem: o fluxo fica escondido na herança, e pra mudar algo precisa saber qual método sobrescrever. Eu ainda usaria função numa view simples ou que foge do padrão de CRUD.
