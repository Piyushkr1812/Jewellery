let btn, Address, prodoct, cut;
btn = document.getElementsByClassName("hoverbtn")[0];
Address = document.querySelectorAll("div.Addresses")[0];
prodoct = document.querySelectorAll("div.product");

btn.addEventListener(
    'click',
    () => {
        for (let i = 0; i < prodoct.length; i++) {
            Address.style.display = "block";
            prodoct[i].style.display = "block";
        }; 
        
    }
);
/** when the user clicks twice at a second it will hide the menu 
 *  dbl === double click 
 */
btn.addEventListener(
    'dblclick',
    () => {
        for (let i = 0; i < prodoct.length; i++) {
            Address.style.display = "none";
            prodoct[i].style.display = "none";
        }
    }
)