function getResidentType(i)
{
	var r=true;
	if(i==0 && isFormUpdated())
	{
		r=confirm("Are you sure you want to change the type field ?? You will loose all the changes you have made.!");
	}
	if(r==true)
	{
		var x=document.getElementById("residentTypeSelect");
		var residentType=(x.options[x.selectedIndex].text);
		if(x.selectedIndex==i+0){
			self.location="register_student";}
		else if(x.selectedIndex==i+1){
			self.location="register_faculty";}
		else if(x.selectedIndex==i+2){
			self.location="register_staff";}
		else if(x.selectedIndex==i+3){
			self.location="register_other";}
		else{
			self.location="typeError";}
		}
}

function isFormUpdated()
{
	// check changes in all input field
	var inputs, index;
	inputs = document.getElementsByTagName('input');
	for (index = 0; index < inputs.length; ++index)
	{
		// deal with inputs[index] element.
		var name = inputs[index];
		if (name.value != name.defaultValue) return true;
	}
	
	// // check changes in all select field
	inputs = document.getElementsByTagName('select');
	var sum=0;
	for (index = 0; index < inputs.length; ++index)
	{
		// deal with inputs[index] element.
		var name = inputs[index];
		if (!name.options[name.selectedIndex].defaultSelected) sum+=1;;	//the type field will always change , hence requiring to count
	}
	if ( sum > 1)return true;
	return false;
}
