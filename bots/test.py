﻿{% extends "base.html" %}
{% load static %}

{% block header %}

<div class="pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">

  <h1 class="display-4">Техническая поддержка</h1>
  
  <p class="lead">Здесь Вы можете к нам обратиться с вопросами и предложениями.</p>
  
</div>

{% endblock %}

{% block content %}

<div class="card-deck mb-3 text-center">
  
    <div class="card mb-4 shadow-sm">
      <div class="card-header">
        <h4 class="my-0 font-weight-normal">Напишите</h4>
      </div>
      <div class="card-body">
        <form method="post">
			<input type="hidden" name="login" id="login" value="test">
			
			<label>Ваш Email:</label><br>
			<input type="text" placeholder="Email" name="email" id="email" maxlength="100"><br><br>
			
			<label>Текст сообщения:</label><br>
			<div contenteditable="true">
				<textarea placeholder="Здесь напишите Ваш вопрос или предложение" name="message" id="message" maxlength="1500" wrap="soft"></textarea>
			</div>
			<br>
			
			<button type="button" class="btn btn-lg btn-block btn-outline-primary">Отправить</button>
		</form>
      </div>
    </div>
		
</div>

  
{% endblock %}


