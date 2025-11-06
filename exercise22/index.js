// const para = document.getElementById("main")
const myText = document.getElementById('myText')
const add = document.getElementById('add')
const remove = document.getElementById('remove')
const clear = document.getElementById('clear')

function addText(){
    const para = document.createElement('p')
    para.innerText= myText.value;
    document.getElementById('text').appendChild(para)
    const paragraphs = JSON.parse(localStorage.getItem('paragraphs')) || [];
    paragraphs.push(myText.value)
    localStorage.setItem('paragraphs', JSON.stringify(paragraphs))
}
add.addEventListener("click",addText)

function removeText(){
    const container = document.getElementById('text');
    const paras = container.getElementsByTagName('p');
    if (paras.length > 0) {
        container.removeChild(paras[paras.length - 1]);
        const paragraphs = JSON.parse(localStorage.getItem('paragraphs')) || [];
        paragraphs.pop(myText.value)
        localStorage.setItem('paragraphs', JSON.stringify(paragraphs))  
}
}
function clearText(){
    const container = document.getElementById('text');
    const paras = container.getElementsByTagName('p');
    while (paras.length > 0) {
        container.removeChild(paras[0]);
        localStorage.removeItem('paragraphs',paras[0])
    }
}


remove.addEventListener("click",removeText)
clear.addEventListener('click',clearText)