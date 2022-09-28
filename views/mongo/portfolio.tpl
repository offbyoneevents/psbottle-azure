% rebase("mongo/base.tpl")

<ul>
% for investment in investments:
    <li>
        {{ investment["coin_id"] }} - ${{ investment["value"] }} 
    </li>
% end
</ul>