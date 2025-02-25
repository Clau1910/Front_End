const { criarProduto } = require('./controllers/ProdutoController');
 
const produto = criarProduto('Caneta Azul', 1.50, 'Caneta azul para escrever.');
console.log(`Produto Criado: ${produto.nome} - R$${produto.preco} - ${produto.descricao}`);
