

let searchForm = document.getElementById('searchForm');
let pageLinks = document.getElementsByClassName('page-link');

if (searchForm) {
    for (let i = 0; i < pageLinks.length; i++) {
        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault();

            let page = this.dataset.page;

            // FIX 1: use backticks
            searchForm.innerHTML += `<input value="${page}" name="page" hidden />`;

            // FIX 2: submit form
            searchForm.submit();
        });
    }
}
