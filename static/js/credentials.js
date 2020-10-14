window.onload = () => {

    const author = ['Gabriel Laurindo', 'Bruno Jaccoud'];
    const hiperlink = ['https://github.com/gabriel-laurindo-1', "https://github.com/jaccoudb"];

    let year_value = new Date().getFullYear();

    // Configurações de estilo no body para o rodapé
    // ficar no final da página
    document.body.style.position = 'relative';
    document.body.style.minHeight = '100vh';

    // Identificação do elemento footer
    var _credential = document.getElementById('my_credential');
    _credential.style = "position: relative; bottom: 0;\
    border-top: 1px solid rgba(0, 0, 0, 0.5); width: 100%;\
    text-align: center; padding: 10px 0; opacity: 0.8;\
    text-decoration: none;";

    // Criação do footer personalizado
    _credential.innerHTML = '<p> Copyright &copy ' + year_value +
        ', Desenvolvido por <a href="' + hiperlink[0] + '" target="_blank" id="dev_link">' + author[0] + '<a/> e \
        <a href="' + hiperlink[1] + '" target="_blank" id="dev_link">' + author[1] + '<a/>. </p>';

    let link = document.getElementById('dev_link');
    link.style = "text-decoration: none; color: #000000;";

};