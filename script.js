let btns = document.querySelectorAll("#btn");
let msg = document.querySelector("#winLose");
let resetBtn = document.querySelector("#reset");
let playerX = true;

const winPatterns = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7],[2,5,8], [0,4,8], [2,4,6]];

btns.forEach((btn) => {
    btn.addEventListener("click", () =>{
        console.log("Button was clicked.");
        if(playerX){
            btn.innerText = "X";
            playerX = false;
        }
        else{
            btn.innerText = "O";
            playerX = true;
        }
        btn.disabled = true;
        chkWinner();
    });
});

const chkWinner = () =>{
    for(let pattern of winPatterns){
        let val1 = btns[pattern[0]].innerText;
        let val2 = btns[pattern[1]].innerText;
        let val3 = btns[pattern[2]].innerText;
    if(val1 != "" && val2 != "" && val3 != ""){
        if((val1 === val2) && (val2 === val3)){
            msg.innerText = "Winner: "+ val1;
            showWinner(val1);
            disableBtns();
        }
    }
}
};

const showWinner = (winner) =>{
    msg.innerText = "Winner: "+winner;
};

const disableBtns = () =>{
    for(btn of btns){
        btn.disabled = true;
    }
}

const enableBtns = () =>{
    for(btn of btns){
        btn.disabled = false;
        btn.innerText = "";
    }
}

const resetGame = () =>{
    enableBtns();
    msg.innerText = "";
    playerX = true;
    btns.innerText = "";
}

resetBtn.addEventListener("click",resetGame);