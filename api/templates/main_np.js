function rate(){
 // document.body.style.opacity = 0.5;
  cc = `
 <div class="rate">
   <h2 class="hrate" style="margin: 2px auto">Seberapa berguna tool ini?</h2>
   <form >
 <div class="value" name='vrate'>0</div>
 <input type="range" min="0" max="5" step="0.01" value="0" name='valrate' class='valrate'>
 <br />
 <h3 class="hr" style="text-align: center">Rate</h3>
 <div class="rname">
   
   <div class="btn-group pilcov" role="group" aria-label="Basic example">
     
	  <button type="button" class="btn btn-light border shadow-sm kdl" onclick="nn('anonim')" style="background-color:gray ;">Anonim</button>
	  <button type="button" class="btn btn-light border shadow-sm kbar" onclick="nn('profil')">Nama</button>
	  
	</div>
	
	
<div class="kr">
  
<input class="form-control rn krn" type="text" placeholder="Namamu.." aria-label="Namamu.." name='nama' value='Anonim'>

</div>
 </div>
 
 
<div class="mb-3">
  <label for="exampleFormControlTextarea1" class="form-label">Ulasan</label>
  <textarea class="form-control ulas" id="exampleFormControlTextarea1" rows="3" placeholder="Lewati aja .." value='Bisa dilewat..' name='ulas'></textarea>
</div>

<div class="p-2 w-full">
            <button class="flex mx-auto text-white bg-primary border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg" onclick="na()">
              <font style="vertical-align: inherit;">
                <font style="vertical-align: inherit;">Kirim</font>
              </font>
            </button>
          </div>
          
</form>

 </div>
 `;
 let rate = document.querySelector('.rate');
 
 let rt = document.querySelector('.rt');
 rt.innerHTML = cc;
 
 // rate.style.opacity = 1;
 
 var elem = document.querySelector('input[type="range"]');

var rangeValue = function() {
  var newValue = elem.value;
  var target = document.querySelector('.value');
  target.innerHTML = newValue;
}

elem.addEventListener("input", rangeValue);


}
function nn(crn) {
  if (crn == 'anonim') {
    let kr = document.querySelector('.kr');
    kr.innerHTML = `
<input class="form-control rn krn" type="text" placeholder="Default input" aria-label="default input example" disabled >`;
    let kdl = document.querySelector('.kdl');
    let kbar = document.querySelector('.kbar');
    kdl.style.background = 'white';
    kbar.style.background = 'gray';

  } else {
    let kbar = document.querySelector('.kbar');
    let kdl = document.querySelector('.kdl');
    kdl.style.background = 'gray';
    kbar.style.background = 'white';

    let kr = document.querySelector('.kr')
    kr.innerHTML = `
<input class="form-control rn krn" type="text" placeholder="Default input" aria-label="default input example">`;

  }
}

function na(){
    let rate = document.querySelector('.rate');
    rate.style.display = 'none';
    //document.body.style.opacity = 1;
}

let wak = document.querySelector('.wak');

let w = '';

// for (let i = 0; i > -12; i--) {
//   w += document.referrer[i];
// };

if(w == '0'){
  
for(let i=0;i <= 7;i++){
setTimeout(()=>{
    wak.innerHTML = `${7 - i}`
  }, i * 1000)
}
  
  
setTimeout(() => {
    rate();
}, 7000)

}else{
  alert(w)
}