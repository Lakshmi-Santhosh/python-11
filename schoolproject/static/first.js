var mealsByCategory = {
  A: ["Bsc computerscience","Msc computerscience","BCA"],
  B: ["BCOM","MCOM"],
  C: ["BSC humanities","MSC Humanities"],
  D: ["Bsc biomaths", "Msc biomaths"],
  E: ["BSC chemistry","bsc industrial chem"],
}

function changecat(value) {
  if (value.length == 0) document.getElementById("category").innerHTML = "<option></option>";
  else {
    var catOptions = "";
    for (categoryId of mealsByCategory[value]) {
      catOptions += "<option>" + categoryId + "</option>";
    }
    document.getElementById("category").innerHTML = catOptions;
  }
}