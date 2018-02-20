<script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
<script type="text/javascript">

var userid = (geturl()["userid"]);
var base_url = "http://127.0.0.1:8000/leave/"; 
var id="&id="+userid; 

    function geturl(varname){
        var url = window.location.href;
        var vars = {}
        var hashes = url.split("?")[1];
        var hash = hashes.split("&");
        for (i=0; i<hash.length; i++){
            params = hash[i].split("=");
            vars[params[0]] = params[1];
        }return vars;
    }

    function get_request_info(){
        $(document).ready(function(){
        $.ajax({
            type: "GET",
            dataType: "json",
            url: base_url+"pending/requests/?format=json"+id,
            success: function(data){
                $("#name").val(data.name.name)
                $("#from_date").val(data.from_date)
                $("#to_date").val(data.to_date)
                $("#no_days").val(data.no_days)
                $("#leave_type").val(data.leave_type.catagory)
                $("#reason").val(data.reason)
                }     
            });
        });
    }
</script>