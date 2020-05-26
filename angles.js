var theta1 = 0
var theta2 = 0
var speed1 = 0.1
var speed2 = 0.3
var left_offset = 650
var top_offset = 150
var l = 150
var x1, y1, x2, y2
var prev_x, prev_y
var i = 0

fetch("http://127.0.0.1:5000/")
.then(res => res.json())
.then(obj => {

    angles = obj["angles"]      

    theta1 = angles[i][0]
    theta2 = angles[i][1]
    x1 = left_offset +  l * Math.sin(theta1)
    y1 = top_offset + l * Math.cos(theta1)
    x2 = x1 + l * Math.sin(theta2)      
    y2 = y1 + l * Math.cos(theta2)
    prev_x = x2
    prev_y = y2
    setInterval(function(){ 
        //theta1 += speed1
        //theta2 += speed2
        theta1 = angles[i][0]
        theta2 = angles[i][1]
                    
        var pend1 = document.getElementById("first_pend")
        var pend2 = document.getElementById("sec_pend")
        x1 = left_offset +  l * Math.sin(theta1)
        y1 = top_offset + l * Math.cos(theta1)
        x2 = x1 + l * Math.sin(theta2)      
        y2 = y1 + l * Math.cos(theta2)
                    
        pend1.setAttribute("cx",x1)
        pend1.setAttribute("cy",y1)
        pend2.setAttribute("cx", x2)
        pend2.setAttribute("cy", y2)
                    
        var line1 = document.getElementById("line1")
        var line2 = document.getElementById("line2")
                    
        line1.setAttribute("x1",left_offset)
        line1.setAttribute("y1",top_offset)
        line1.setAttribute("x2", x1)
        line1.setAttribute("y2", y1)

                    
        line2.setAttribute("x1",x1)
        line2.setAttribute("y1",y1)
        line2.setAttribute("x2",x2)
        line2.setAttribute("y2",y2)
                    
        /*var dot = document.createElementNS('http://www.w3.org/2000/svg',"circle")
        dot.setAttribute("cx",x2)
        dot.setAttribute("cy",y2)
        dot.setAttribute("r", "1")
        dot.setAttribute("fill", "black")
        dot.setAttribute("stroke", "black")
        dot.setAttribute("stroke-width", 1)*/
                    
        var path = document.createElementNS('http://www.w3.org/2000/svg',"line")
        path.setAttribute("x1",prev_x)
        path.setAttribute("y1",prev_y)
        path.setAttribute("x2",x2)
        path.setAttribute("y2",y2)
        path.setAttribute("style", "stroke:rgb(0,0,0);stroke-width:1")
                    
        prev_x = x2
        prev_y = y2
        //document.getElementsByTagName("svg")[0].insertBefore(dot, pend1)
        document.getElementsByTagName("svg")[0].insertBefore(path,pend1)
        i++
    }, 25);
})