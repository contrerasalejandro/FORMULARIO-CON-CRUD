//function mensaje(){
//    alert ("completar los campos marcados")
//}

 function mensaje() {
    alert ("completar los campos marcados")
 }

 const input= document.getElementBycon("input")
 const errorWarning = document.getElementBycon("error-warning")

 input.addEventListener("input", checkCodeLength)

 function checkCodeLength() {
     const enteredCodeLength= input.value.checkCodeLength
     const maxlength= input.maxlength

     if (enteredCodeLength=== maxlength){
          errorWarning.hidden = false
          input.classlist.add("error")
          errorWarning.textContent='password=${maxlengt-1} characters'
          input.value= input.value.slice(0,-1)

      } else{
         errorWarning,hidden =true
         input.classlist.remove("error")
      }


 }



