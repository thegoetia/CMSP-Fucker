<h1>CMSP Fucker</h1>

<p>CMSP Fucker é um script em Python para verificar respostas a questões em tarefas do CMSP. O script recebe IDs de tarefa e questão do usuário e envia as respostas em formato JSON, formatando a resposta para o usuário.</p>

<h2>Índice</h2>
<ul>
    <li><a href="#pre-requisitos">Pré-requisitos</a></li>
    <li><a href="#instalacao">Instalação</a></li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#exemplo-de-execucao">Exemplo de Execução</a></li>
    <li><a href="#observacoes">Observações</a></li>
</ul>

<h2 id="pre-requisitos">Pré-requisitos</h2>
<p>Para rodar este script, você precisa ter o Python 3.x instalado no seu sistema. Também é necessário instalar a biblioteca <code>requests</code>, que é usada para fazer requisições HTTP.</p>

<p>Você pode instalar a biblioteca <code>requests</code> executando o seguinte comando:</p>
<pre><code>pip install requests</code></pre>

<h2 id="instalacao">Instalação</h2>
<ol>
    <li>Clone este repositório ou baixe os arquivos diretamente.
        <pre><code>git clone https://github.com/thegoetia/CMSP-Fucker.git</code></pre>
    </li>
    <li>Navegue até o diretório onde o script está localizado.
        <pre><code>cd CMSP-Fucker</code></pre>
    </li>
    <li>Certifique-se de que a biblioteca <code>requests</code> está instalada.
        <pre><code>pip install requests</code></pre>
            <li>Certifique-se de que a biblioteca <code>colorama</code> está instalada.
        <pre><code>pip install colorama</code></pre>
    </li>
</ol>

<h2 id="uso">Uso</h2>
<p><strong>Execução do Script</strong>:</p>
<p>Ao rodar o script, ele solicitará os seguintes valores:</p>
<ul>
    <li>ID da tarefa</li>
    <li>ID da questão</li>
    <li>API Key</li>
</ul>

<p><strong>Comando para executar o script</strong>:</p>
<pre><code>python cmsp.py</code></pre>

<p>O script irá então solicitar os IDs e a chave da API no terminal:</p>
<pre><code>Digite o ID da tarefa:
Digite o ID da questão:
Digite a API Key:
</code></pre>

<p>Após fornecer as informações, o script enviará os dados para a API e retornará o resultado da verificação.</p>

<h2 id="exemplo-de-execucao">Exemplo de Execução</h2>
<pre><code>$ python cmsp.py

      ____ __  __ ____  ____    _____ _   _  ____ _  _______ ____  
     / ___|  \/  / ___||  _ \  |  ___| | | |/ ___| |/ / ____|  _ \ 
    | |   | |\/| \___ \| |_) | | |_  | | | | |   | ' /|  _| | |_) |
    | |___| |  | |___) |  __/  |  _| | |_| | |___| . \| |___|  _ < 
     \____|_|  |_|____/|_|     |_|    \___/ \____|_|\_\_____|_| \_\

Digite o ID da tarefa: 53511868
Digite o ID da questão: 139544577
Digite a API Key: sua-api-key-aqui

Verificando a questão 139544577 da tarefa 53511868...

Score: 0
Comentário: 
- A alternativa (A) está incorreta, porque Brás Cubas não é descrito como uma criança exemplar. Ao contrário, ele demonstra crueldade, egoísmo e falta de respeito pelos escravizados...
</code></pre>

<h2 id="observacoes">Observações</h2>
<ul>
    <li><strong>API Key Válida</strong>: Certifique-se de inserir uma <strong>API Key válida</strong> no momento da execução, pois ela é necessária para a autenticação no serviço da API.</li>
    <li><strong>Formato do Payload</strong>: O script foi projetado para funcionar com uma API específica, que deve estar configurada para receber as requisições corretamente no formato JSON.</li>
    <li><strong>Tratamento de Erros</strong>: O script inclui tratamento básico de erros para informar quando há problemas na requisição.</li>
</ul>

<h2>Contribuições</h2>
<p>Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou novos recursos para este script, sinta-se à vontade para abrir um pull request ou relatar um problema (issue).</p>
