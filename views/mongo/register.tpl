% rebase("mongo/base.tpl")

<form method="post">
    <div class="form-row">
        <label for="username">Username: </label>
        <input type="text" name="username" />
    </div>
    <div class="form-row">
        <label for="password">Password: </label>
        <input type="password" name="password" />
    </div>
    <div class="form-row">
        <label for="confirm">Confirm: </label>
        <input type="password" name="password2" />
    </div>
    <div class="form-row">
        <input type="submit" value="Register" />
    </div>
</form>
