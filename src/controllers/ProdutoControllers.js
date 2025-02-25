const Produto = require('../models/Produto');

function criaProduto(nome, preco, descricao) {
    const novoProduto = new Produto(nome, preco, descricao)
    return novoProduto;
}

module.exports = {criaProduto};