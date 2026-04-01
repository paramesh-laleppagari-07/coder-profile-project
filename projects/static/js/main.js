
    //GET SEARCH FORM AND LINKS
    let searchForm = document.getElementById('searchForm');
    let pageLinks = document.getElementsByClassName('page-link');

   // ENSURE SEARCH FORM EXISTS
    if (searchForm) {
        // Add event listener to page links
        for (let i = 0; i < pageLinks.length; i++) {
            pageLinks[i].addEventListener('click', function (e) {
                e.preventDefault();
                // add data attribute
                let page =this.dataset.page;
                //get the data search input to form
                searchForm.innerHTML += '<input value=${page} name="page" hidden />  ';
                //submit the form

    
            });
        }
    }

