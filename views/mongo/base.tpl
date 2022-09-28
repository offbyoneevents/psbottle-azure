% rebase("base.tpl")
% setdefault("current_user", None)

<aside>
    <ul>
        % if current_user is not None:
            <li><a href="/mongo/portfolio">Portfolio</a></li>
            <li><a href="/mongo/buy">Buy</a></li>
            <li><a href="/mongo/sell">Sell</a></li>
            <li><a href="/mongo/logout">Logout</a></li>
        % else:
            <li><a href="/mongo/login">Login</a></li>
            <li><a href="/mongo/register">Register</a></li>
        % end
    </ul>
</aside>

<div class="container">
    {{!base}}
</div>