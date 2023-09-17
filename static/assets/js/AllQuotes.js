// Developed By Saurabh Upadhyay

function pic(val){
	
            var element = $("."+val);   
            var getCanvas; 			
			
				html2canvas(element, { 
                    onrendered: function(canvas) {
					getCanvas = canvas; 
					var imgageData = getCanvas.toDataURL("image/png");
					var newData = imgageData.replace(/^data:image\/png/, "data:application/octet-stream"); 
					var a = document.createElement("a"); //Create <a>
					a.href = newData; //Image Base64 Goes here
					a.download = "AllQuotes.png"; //File name Here
					a.click();
					
				}
                 
            }); 
	
          
            
			
		}
		
