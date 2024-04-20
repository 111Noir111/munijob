(function(){

    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion=confirm('¿Esta seguro de eliminar este trabajo?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    }); 


    const btnCerrar = document.querySelectorAll(".alert .btn-close");

    btnCerrar.forEach(btn => {
        btn.addEventListener('click', (e) => {
            btn.closest('.alert').style.display = 'none';
        });
    });
    
})();