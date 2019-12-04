  /* Configuracion de FIREBASE
  var firebaseConfig = {
    apiKey: "AIzaSyCS3cWvtoXVCT1yxs-SC1CiSYzeYuGkwrc",
    authDomain: "vans-comit.firebaseapp.com",
    databaseURL: "https://vans-comit.firebaseio.com",
    projectId: "vans-comit",
    storageBucket: "vans-comit.appspot.com",
    messagingSenderId: "1030828373346",
    appId: "1:1030828373346:web:ce419539bc7b52f479683b",
    measurementId: "G-6QQZBF6CYE"
  };
  // Inicializar Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();*/

    /* Efecto para el Nav*/
    $('#toggle-menu').click(function(){
        $(this).next().slideToggle();
    })


    function dar_asiento(id,value){
        // Confirmación del asiento elegido (if true, hace esto, sino no hace nada)
        if(confirm('El lugar elegido es el Nro: '+value+'.\n¿Desea reservar ese lugar?')){
            // Array de asientos totales
            var asientos_totales = ["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10","a11","a12","a13","a14","a15","a16","a17","a18","a19"];
            // Recorre el array (el loop) del 0 al total del array y va sumando 1 a la variable I (que luego es el indice del array)
            for (i = 0; i < asientos_totales.length; i++){
                // Le quita a todos los hacientos la propiedad de ser clikeado
                var selec_asiento = document.getElementById(asientos_totales[i]).toggleAttribute("onclick");
                // Cambia el color de fondo del asiento seleccionado
                var selec_asiento = document.getElementById(id).className = "inactivo";
            }
            // Selecciona el input del asiento elegido
            var asiento = document.querySelector("#asiento_elegido")
            // Inserta el valor del asiento elegido en el input correspondiente    
            asiento.innerHTML = `
            <input type="hidden" id="nroElegido" value="${value}" name="asiento">
            `;
        }
    }