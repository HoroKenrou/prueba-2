function checkRut(rut) {

    var valor = rut.value.replace('.','');

    valor = valor.replace('-','');
    

    cuerpo = valor.slice(0,-1);
    dv = valor.slice(-1).toUpperCase();
    

    rut.value = cuerpo + '-'+ dv
    

    if(cuerpo.length < 7) 
	{ 
		document.getElementById("rut").focus(); 
		document.getElementById("rut").style.color="red";
		
		
	
	}
	else
	{
		document.getElementById("rut").style.color="green";	
		
    }
	

    suma = 0;
    multiplo = 2;
    
  
    for(i=1;i<=cuerpo.length;i++) {
    
       
        index = multiplo * valor.charAt(cuerpo.length - i);
        
     
        suma = suma + index;
        
   
        if(multiplo < 7) { multiplo = multiplo + 1; } else { multiplo = 2; }
  
    }
    

    dvEsperado = 11 - (suma % 11);
    
    dv = (dv == 'K')?10:dv;
    dv = (dv == 0)?11:dv;
    
    if(dvEsperado != dv) 
	{ 
		
		document.getElementById("rut").focus(); 
		document.getElementById("rut").style.color="red";
		
		
	}
	else
	{
		document.getElementById("rut").style.color="green";
		
	}
	
}


function ValidarNombre(nombre)
{
	
	var nombres= document.getElementById("nombre").value;
	
	if(nombres.length<3 | nombres.length>40)
	{
		
		document.getElementById("nombre").focus();
		document.getElementById("nombre").style.color="red";
		
	}
	else
	{
	
		document.getElementById("nombre").style.color="green";
		
	}	
}


function Validartelefono()
{

	var numero = document.getElementById("telefono").value;
	
	if (isNaN(numero))
	{
		
		document.getElementById("telefono").focus();
		document.getElementById("telefono").style.color="red";				
	}
	else
	{	
		
		document.getElementById("telefono").style.color="green";	
		
	}
}



function ValidarFecha()

{
	
	var fecha= document.getElementById("calendar").value;
	
	if (fecha.substr(6,4)>2000)
	{
		
		document.getElementById("calendar").focus();
		document.getElementById("calendar").style.color="red";	
		
	}
	else
	{
		
		document.getElementById("calendar").style.color="green";
		
	}
	
	
	
	
	
}


