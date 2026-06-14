document.addEventListener('DOMContentLoaded', function() {
    const badge = document.getElementById('notify-badge');
    const menu = document.getElementById('notifications-menu');
    const list = document.getElementById('notifications-list');
    const bell = document.getElementById('bell-icon');

    // باز و بسته کردن منو
    bell.addEventListener('click', () => {
        menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
    });

    function updateNotifications() {
        fetch('/api/waiter/active-calls/')
            .then(res => res.json())
            .then(calls => {
                const count = calls.length;

                // آپدیت عدد
                badge.style.display = count > 0 ? 'block' : 'none';
                badge.textContent = count;

                // رندر کردن لیست
                list.innerHTML = '';
                calls.forEach(call => {
                    const item = document.createElement('div');
                    item.style = "padding:10px; border-bottom:1px solid #eee; display:flex; justify-content:space-between; align-items:center;";
                    item.innerHTML = `
                        <span>${call.table_label}</span>
                        <button onclick="resolveCall(${call.id})" style="background:#28a745; color:white; border:none; padding:5px 10px; border-radius:5px; cursor:pointer;">✓</button>
                    `;
                    list.appendChild(item);
                });
            });
    }

    // تابع گلوبال برای تیک زدن
    window.resolveCall = function(id) {
        fetch(`/api/waiter/resolve/${id}/`, {
            method: 'POST',
            headers: {'X-CSRFToken': getCookie('csrftoken')}
        }).then(() => updateNotifications());
    };

    setInterval(updateNotifications, 5000);
    updateNotifications();
});

// تابع دریافت CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}