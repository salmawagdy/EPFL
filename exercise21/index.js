const myPar = document.getElementById("myPar")
const myButton = document.getElementById("myButton")
const myText = document.getElementById("myText")

function changePara(){
    myPar.innerText = myText.value;
}
myButton.addEventListener("click",changePara)
