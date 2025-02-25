const { criarProduto } = require('../src/controllers/ProdutoController');

test('Criação de produto', () => {
    const produto = criarProduto('Lápis', 0.50, 'Lápis para desenho.');
    expect(produto.nome).toBe('Lápis');
    expect(produto.preco).toBe(0.50);
    expect(produto.descricao).toBe('Lápis para desenho.');
});
