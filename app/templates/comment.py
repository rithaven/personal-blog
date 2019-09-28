{% extends 'base.html'%}

{% block content %}
<div class="container-fluid ">
 <div class="row">
  <div class="col-sm-4">
    <img src="{{comment.image_path}}" class="img-responsive">
  </div>

  <div class="col-sm-8">
    {{format_comment|safe}}
  </div>
 </div>
</div>
{%endblock%}