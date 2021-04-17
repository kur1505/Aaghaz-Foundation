console.log('Logging');


function getSTBbyID() {
    var stdData=$('#sltSTB').val();
    _success = function (res) {
       // console.log(res);
        var data = res[0].fields;
        $('#stbDOP').val(data.DOP);
        $('#stbIssueDate').val(data.issue_date);
        $('#stbModel').val(data.model_number);
        $('#stbType').val(data.Type);
        console.log(data);
        $('#stbRemark').val(data.remark);
        $('#stbBox').val(data.box_type);
        $('#stbStatus').val(data.status);
        console.log(data);
    }
    _error = function (error) {
        console.log(error);
 
    }
   
 
    callAjaxGet('/getSTBbyID/'+stdData+'/', '', _success, _error, false, '');
 
}

function getNodebyID() {
    var stdData=$('#sltNode').val();
    _success = function (res) {
        var data = res[0].fields;
        $('#nodeModel').val(data.model_number);
        $('#nodeRemark').val(data.remark);
        $('#nodeSTBCount').val(data.STB_count);
        $('#nodeArea').val(data.area);
        $('#nodeStatus').val(data.status);
        $('#nodeIssueDate').val(data.issue_date);
        $('#nodeDOP').val(data.DOP);
        console.log(data);
    }
    _error = function (error) {
        console.log(error);
 
    }
   
    callAjaxGet('/getNodebyID/'+stdData+'/', '', _success, _error, false, '');
 
}

function getRouterbyID() {
    var stdData=$('#sltRouter').val();
    _success = function (res) {
        console.log('Success');
        var data = res[0].fields;
        $('#routerMake').val(data.make);
        $('#routerRemark').val(data.remark);
        $('#routerModel').val(data.model_number);
        $('#routerMac').val(data.mac_id);
        $('#routerIP').val(data.ip_address);
        $('#routerStatus').val(data.status);
        $('#routerType1').val(data.type1);
        $('#routerRType').val(data.router_type);
        $('#routerDOP').val(data.DOP);
        $('#routerIssue').val(data.issue_date);
        console.log(data);
    }
    _error = function (error) {
        console.log('Error is');
        console.log(error);
 
    }
   
    callAjaxGet('/getRouterbyID/'+stdData+'/', '', _success, _error, false, '');
 
}