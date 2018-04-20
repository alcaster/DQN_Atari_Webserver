const $ = id => document.getElementById(id);

document.addEventListener("DOMContentLoaded", function (event) {
    let nodes = $('gameButtons').childNodes;
    for (let i = 0; i < nodes.length; i++) {
        if (nodes[i].nodeName.toLowerCase() === 'button') {
            nodes[i].addEventListener("click", callGame);
        }
    }

    $("stop_button").addEventListener("click", () => {
        $("preview").removeChild($("preview").firstElementChild);
    });
});

function callGame() {
    let e = document.createElement('img');
    try {
        e.src = Flask.url_for(this.id);
    }
    catch (e) {
        console.log(e.message);
    }
    finally {
        e.classList.add("preview_style");
        $("preview").appendChild(e);
    }
}