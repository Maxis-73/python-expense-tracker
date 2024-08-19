<h1 class="code-line" data-line-start="0" data-line-end="1"><a id="Expense_Tracker_CLI_0"></a>Expense Tracker CLI</h1>
<p class="has-line-data" data-line-start="1" data-line-end="2">Instructions</p>
<ol>
<li class="has-line-data" data-line-start="2" data-line-end="5">
<p class="has-line-data" data-line-start="2" data-line-end="4">Clone the repository:<br>
<code>git clone https://github.com/Maxis-73/python-expense-tracker.git</code></p>
</li>
<li class="has-line-data" data-line-start="5" data-line-end="9">
<p class="has-line-data" data-line-start="5" data-line-end="8">Create virtual enviroment<br>
If you do not have virtualenv installed, you can install it with the following command: <code>pip install virtualenv</code><br>
Create virtual enviroment: <code>virtualenv vitual_enviroment_name</code></p>
</li>
<li class="has-line-data" data-line-start="9" data-line-end="13">
<p class="has-line-data" data-line-start="9" data-line-end="12">Activate virtual enviroment<br>
In Linux and Mac: <code>source vitual_enviroment_name/bin/activate</code><br>
In Windows: <code>.\vitual_enviroment_name\Scripts\activate</code></p>
</li>
<li class="has-line-data" data-line-start="13" data-line-end="16">
<p class="has-line-data" data-line-start="13" data-line-end="15">Install dependencies<br>
Run this command: <code>pip install -r requirements.txt</code></p>
</li>
</ol>
<p class="has-line-data" data-line-start="16" data-line-end="17">Run the project</p>
<ol>
<li class="has-line-data" data-line-start="17" data-line-end="18">List all expenses: <code>python src/app.py list</code></li>
<li class="has-line-data" data-line-start="18" data-line-end="19">Create a new expense: <code>python src/app.py add --description &quot;Dinner&quot; --amount 100</code></li>
<li class="has-line-data" data-line-start="19" data-line-end="20">Update an expense: <code>python src/app.py update --id 11 --description &quot;Dinner&quot; --amount 250</code></li>
<li class="has-line-data" data-line-start="20" data-line-end="21">Delete an expense: <code>python src/app.py delete --id 11</code></li>
<li class="has-line-data" data-line-start="21" data-line-end="22">Summary of all expenses: <code>python src/app.py summary</code></li>
<li class="has-line-data" data-line-start="22" data-line-end="23">Summary by month: <code>python src/app.py summary-by-month --month 11</code></li>
</ol>
</body></html>