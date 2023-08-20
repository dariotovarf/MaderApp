(function () {
    const btnEliminar = document.querySelectorAll(".btnEliminar");
  
    btnEliminar.forEach((btn) => {
      btn.addEventListener("click", (e) => {
        const confirmacion = confirm("¿Esta seguro de eliminar?");
        if (!confirmacion) {
          e.preventDefault();
        }
      });
    });
  })();