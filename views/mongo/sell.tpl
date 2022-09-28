% rebase("mongo/base.tpl")

<form method="post">
    <div class="form-row">
        <label for="coin_id">Coin Id</label>
        <select name="coin_id">
            % for c in owned_coins:
                <option value="{{c}}">{{c}}</option>
            % end
        </select>
    </div>
    <div class="form-row">
        <label for="quantity">Quantity</label>
        <input type="text" name="quantity" />
    </div>
    <div class="form-row">
        <input type="submit" value="Sell" />
    </div>
</form>

