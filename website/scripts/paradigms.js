//    Written by: Levi Biasco (lbiasco)
//    Updated on: 4/23/201

function Item()
{
    this.addToDocument = function()
        {
            document.body.appendChild(this.item);
        }
}

function Label()
{
    this.createLabel = function(text, id)
        {
            this.item = document.createElement("p");
            this.item.setAttribute("id", id);
            this.item.innerHTML = text;
        },
    this.setLabel = function(id)
        {
            this.item = document.getElementById(id);
        },
    this.setText = function(text)
        {
            this.item.innerHTML = text;
        }
}
Label.prototype = new Item();

function Button()
{
    this.createButton = function(text, id)
        {
            this.item = document.createElement("button");
            this.item.setAttribute("id", id);
            this.item.innerHTML = text;
        },
    this.setButton = function(id)
        {
            this.item = document.getElementById(id);
        },
    this.addClickEventHandler = function(handler, args)
        {
            this.item.onmouseup = function() { handler(args); };
        }
}
Button.prototype = new Item();

function Dropdown()
{
    this.createDropdown = function(dict, id, selected)
        {
            this.item = document.createElement("select");
            this.item.setAttribute("id", id);
            for(key in dict)
            {
                var option = document.createElement("option");
                option.text = dict[key];
                option.value = key;
                this.item.add(option);
            }
            this.item.value = selected;
        },
    this.getSelected = function()
        {
            return this.item.value;
        }
}
Dropdown.prototype = new Item();
