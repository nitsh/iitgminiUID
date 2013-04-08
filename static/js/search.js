function getSubField()
{
	var selected ={
		student : false,
		faculty : 0,
		staff : 0,
		others : 0
	};	if( document.criteriaForm.student.checked == true ){
		selected.student = true;
		//alert( "You have checked student." );
	}
	if( document.criteriaForm.faculty.checked == true ){
		selected.faculty = true;
		//alert( "You have checked faculty." );
	}
	if( document.criteriaForm.staff.checked == true ){
		selected.staff = true;
		//alert( "You have checked staff." );
	}
	if( document.criteriaForm.others.checked == true ){
		selected.others = true;
		//alert( "You have checked others." );
	}
    self.location = "{{=URL('getFieldList')}}";
    //field = [ "name", "dob" ];
}
