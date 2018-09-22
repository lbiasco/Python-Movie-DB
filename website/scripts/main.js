//    Written by: Levi Biasco (lbiasco)
//    Updated on: 4/30/2018

var url = "http://student04.cse.nd.edu:52011/";//"http://ash.campus.nd.edu:40001/";
                   
window.onload = function ()
{
    var labelMovie = new Label();
    labelMovie.setLabel("label");
    labelMovie.setText("(PLACEHOLDER LABEL)");

    var labelRating = new Label();
    labelRating.setLabel("rating");
    labelRating.setText("(PLACEHOLDER RATING)");

    var image = document.getElementById("img");

    getRecommendation(labelMovie, image, labelRating);

    var buttonUp = new Button();
    buttonUp.setButton("up");
    args = [5, labelMovie, image, labelRating];
    buttonUp.addClickEventHandler(sendRating, args);

    var buttonDown = new Button();
    buttonDown.setButton("down");
    args = [1, labelMovie, image, labelRating];
    buttonDown.addClickEventHandler(sendRating, args);
}

function sendRating(args)
{
    var data = {};
    data["movie_id"] = args[1].id;
    data["rating"] = args[0];
    var json = JSON.stringify(data);

    var xhr = new XMLHttpRequest();
    xhr.open("PUT", url+"recommendations/11", true);

    xhr.onload = function()
    {
        if(xhr.readyState === 4)
        {
            console.log("PUT_RATINGS: SUCCESS");
            getRecommendation(args[1], args[2], args[3]);
        }
    }
    xhr.send(json);
}

function getRecommendation(mLabel, img, rLabel)
{
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url+"recommendations/11", true);

    xhr.onload = function()
    {
        var resp = JSON.parse(xhr.responseText);
        if(xhr.readyState === 4)
        {
            mLabel["id"] = resp["movie_id"];
            console.log("GET_RECOMMENDATION: SUCCESS");
            update(resp["movie_id"], mLabel, img, rLabel);
        }
    }
    xhr.send(null);
}

function update(mid, mLabel, img, rLabel)
{
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url+"movies/"+mid, true);

    xhr.onload = function()
    {
        var resp = JSON.parse(xhr.responseText);
        //alert(xhr.responseText);
        if(xhr.readyState === 4)
        {
            mLabel.item.innerHTML = resp["title"];
            if(resp["img"] !== undefined) 
                img.src = "http://www.cse.nd.edu/~cmc/teaching/cse30332/images"+resp["img"];
            else
                img.src = "no-poster.jpg";
            getRating(mid, rLabel);
        }
    }
    xhr.send(null);
}

function getRating(id, label)
{
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url+"ratings/"+id, true);

    xhr.onload = function(e)
        {
            var resp = JSON.parse(xhr.responseText);
            if(xhr.readyState === 4)
                label.item.innerHTML = resp["rating"];
        }
    xhr.send(null);
}
