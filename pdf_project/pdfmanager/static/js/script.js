function createNewInputGrp() {
    // First create a DIV element.
	var txtNewInputBox = document.createElement('div');
    var new_chq_no = parseInt($('#total_chq').val())+1;

    // Then add the content (a new input box) of the element.
	//txtNewInputBox.innerHTML = '<div id="ig-new" class="input-group mx-auto"> <input type="file" class="form-control my-2" id="inputGroupFile" name="inputGroup" accept=".pdf"> <input id="ig-del" type="button" class="btn btn-dark" value="x" onclick="removeInputGrp();"/> </div>';
    txtNewInputBox.innerHTML = '<div id="ig-new" class="input-group mx-auto"> <input type="file" class="form-control my-2" id="inputGroupFile" name="inputGroup'+ new_chq_no +' " accept=".pdf"> <input id="ig-del" type="button" class="btn btn-dark" value="x" onclick="removeInputGrp();"/> </div>';
    $('#total_chq').val(new_chq_no)

    // Finally put it where it is supposed to appear.
	document.getElementById("ig").append(txtNewInputBox);
}




function removeInputGrp() {
    const ig = document.getElementById('ig-new');
  ig.remove();
}