$(document).ready(function() {
  $('#search').on('input', function() {
      let name = $('#search').val();
      $.ajax({
          url: '/',
          data: {'query': $(this).val()},
          type: 'POST',
          success: function(response) {
              //alert(response)
              // Accessing the array of food items via response.foodItems
              let foodItems = response.foodItems;
             // 
              // Remove the old table entirely
              $('#table').remove();
              let table = $('<table>').attr('id', 'table').appendTo('#table-container');
              table.empty();
              table.append("<tr><th>שם</th><th>כמות</th><th>נקודות</th><th>קבוצת מזון</th></tr>")
              foodItems.forEach(item => {
                  table.append("<tr><td>" + item.name + "</td><td>" + item.count + "</td><td>" + item.point + "</td><td>" + item.foodType + "</td></tr>");
              });
              table.appendTo('#table-container');
              
          },
          error: function(error) {
              console.log(error);
          }
      });
  });
});
