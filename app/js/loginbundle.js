function login() {
    let logmail = document.getElementById("email").value;
    let logpass = document.getElementById("password").value;
    if(logmail=="admin@mail.fr" && logpass=="admin"){
        document.getElementById('showlogin').hidden = true;
        document.getElementById('asking1').hidden = true;
        document.getElementById('statusheader').innerHTML = "Bienvenue sur votre tableau de bord"

        
        $("#includedContentNavbar").load("./components/navbarcomp.html"); 
        $("#includedContentCharts1").load("./components/chartsbundle.html"); 

    }else{
        document.getElementById("asking1").innerHTML = "Erreur Login Incorrect";
        document.getElementById('asking1').classList.add('alert-danger');
        document.getElementById('asking1').classList.remove('alert-primary')
    }
}