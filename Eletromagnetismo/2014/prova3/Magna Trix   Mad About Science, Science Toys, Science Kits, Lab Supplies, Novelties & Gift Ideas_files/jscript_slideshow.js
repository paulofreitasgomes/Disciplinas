$slideshow = {
    context: false,
    tabs: false,
    timeout: 4500,      // time before next slide appears (in ms)
    slideSpeed: 1500,   // time it takes to slide in each slide (in ms)
    tabSpeed: 1000,      // time it takes to slide in each slide (in ms) when clicking through tabs
    fx: 'fade',   // the slide effect to use
    
    init: function() {
        // set the context to help speed up selectors/improve performance
	if($('#slideshow').length != 0) {
          this.context = $('#slideshow');
        
          // set tabs to current hard coded navigation items
          this.tabs = $('ul.slides-nav li', this.context);
        
          // remove hard coded navigation items from DOM 
          // because they aren't hooked up to jQuery cycle
          this.tabs.remove();
        
          // prepare slideshow and jQuery cycle tabs
          this.prepareSlideshow();
        }
    },
    
    prepareSlideshow: function() {
        // initialise the jquery cycle plugin -
        // for information on the options set below go to: 
        // http://malsup.com/jquery/cycle/options.html
        $('div.slides > ul', $slideshow.context).cycle({
            fx: $slideshow.fx,
            timeout: $slideshow.timeout,
            speed: $slideshow.slideSpeed,
            fastOnEvent: $slideshow.tabSpeed,
            pager: $('ul.slides-nav', $slideshow.context),
            pagerAnchorBuilder: $slideshow.prepareTabs,
            before: $slideshow.activateTab,
            pauseOnPagerHover: true,
            pause: true
        });            
    },
    
    prepareTabs: function(i, slide) {
        // return markup from hardcoded tabs for use as jQuery cycle tabs
        // (attaches necessary jQuery cycle events to tabs)
        return $slideshow.tabs.eq(i);
    },

    activateTab: function(currentSlide, nextSlide) {
        // get the active tab
        var activeTab = $('a[href="#' + nextSlide.id + '"]', $slideshow.context);
        
        // if there is an active tab
        if(activeTab.length) {
            // remove active styling from all other tabs
            $slideshow.tabs.removeClass('on');
            
            // add active styling to active button
            activeTab.parent().addClass('on');
        }            
    }            
};

$tesSlideshow = {
    context: false,
    tabs: false,
    timeout: 7500,      // time before next slide appears (in ms)
    slideSpeed: 1500,   // time it takes to slide in each slide (in ms)
    tabSpeed: 1000,      // time it takes to slide in each slide (in ms) when clicking through tabs
    fx: 'scrollUp',   // the slide effect to use
    
    init: function() {
	if($('#tesSlideshow').length != 0) {
          // set the context to help speed up selectors/improve performance
          this.context = $('#tesSlideshow');
        
          // set tabs to current hard coded navigation items
          this.tabs = $('ul.slides-nav li', this.context);
        
          // remove hard coded navigation items from DOM 
          // because they aren't hooked up to jQuery cycle
          this.tabs.remove();
        
          // prepare tesSlideshow and jQuery cycle tabs
          this.prepareSlideshow();
        }
    },
    
    prepareSlideshow: function() {
        // initialise the jquery cycle plugin -
        // for information on the options set below go to: 
        // http://malsup.com/jquery/cycle/options.html
        $('div.slides > ul', $tesSlideshow.context).cycle({
            fx: $tesSlideshow.fx,
            timeout: $tesSlideshow.timeout,
            speed: $tesSlideshow.slideSpeed,
            fastOnEvent: $tesSlideshow.tabSpeed,
            pager: $('ul.slides-nav', $tesSlideshow.context),
            pagerAnchorBuilder: $tesSlideshow.prepareTabs,
            before: $tesSlideshow.activateTab,
            pauseOnPagerHover: true,
            pause: true
        });            
    },
    
    prepareTabs: function(i, slide) {
        // return markup from hardcoded tabs for use as jQuery cycle tabs
        // (attaches necessary jQuery cycle events to tabs)
        return $tesSlideshow.tabs.eq(i);
    },

    activateTab: function(currentSlide, nextSlide) {
        // get the active tab
        var activeTab = $('a[href="#' + nextSlide.id + '"]', $tesSlideshow.context);
        
        // if there is an active tab
        if(activeTab.length) {
            // remove active styling from all other tabs
            $tesSlideshow.tabs.removeClass('on');
            
            // add active styling to active button
            activeTab.parent().addClass('on');
        }            
    }            
};


$gstSlideshow = {
    context: false,
    tabs: false,
    timeout: 6000,      // time before next slide appears (in ms)
    slideSpeed: 1000,   // time it takes to slide in each slide (in ms)
    tabSpeed: 1000,      // time it takes to slide in each slide (in ms) when clicking through tabs
    fx: 'blindY',   // the slide effect to use
    
    init: function() {
	if($('#gstSlideshow').length != 0) {
          // set the context to help speed up selectors/improve performance
          this.context = $('#gstSlideshow');
          // set tabs to current hard coded navigation items
          this.tabs = $('ul.slides-nav li', this.context);
        
          // remove hard coded navigation items from DOM 
          // because they aren't hooked up to jQuery cycle
          this.tabs.remove();
        
          // prepare gstSlideshow and jQuery cycle tabs
          this.prepareSlideshow();
        }
    },
    
    prepareSlideshow: function() {
        // initialise the jquery cycle plugin -
        // for information on the options set below go to: 
        // http://malsup.com/jquery/cycle/options.html
        $('div.slides > ul', $gstSlideshow.context).cycle({
            fx: $gstSlideshow.fx,
            timeout: $gstSlideshow.timeout,
            speed: $gstSlideshow.slideSpeed,
            fastOnEvent: $gstSlideshow.tabSpeed,
            pager: $('ul.slides-nav', $gstSlideshow.context),
            pagerAnchorBuilder: $gstSlideshow.prepareTabs,
            before: $gstSlideshow.activateTab,
            pauseOnPagerHover: true,
            pause: true
        });            
    },
    
    prepareTabs: function(i, slide) {
        // return markup from hardcoded tabs for use as jQuery cycle tabs
        // (attaches necessary jQuery cycle events to tabs)
        return $gstSlideshow.tabs.eq(i);
    },

    activateTab: function(currentSlide, nextSlide) {
        // get the active tab
        var activeTab = $('a[href="#' + nextSlide.id + '"]', $gstSlideshow.context);
        
        // if there is an active tab
        if(activeTab.length) {
            // remove active styling from all other tabs
            $gstSlideshow.tabs.removeClass('on');
            
            // add active styling to active button
            activeTab.parent().addClass('on');
        }            
    }            
};

$whyShopSlideshow = {
    context: false,
    tabs: false,
    timeout: 8500,      // time before next slide appears (in ms)
    slideSpeed: 2000,   // time it takes to slide in each slide (in ms)
    tabSpeed: 1500,      // time it takes to slide in each slide (in ms) when clicking through tabs
    fx: 'fade',   // the slide effect to use
    
    init: function() {
        if($('#whyShopSlideshow').length != 0) { 
          // set the context to help speed up selectors/improve performance
          this.context = $('#whyShopSlideshow');
          // set tabs to current hard coded navigation items
          this.tabs = $('ul.slides-nav li', this.context);
        
          // remove hard coded navigation items from DOM 
          // because they aren't hooked up to jQuery cycle
          this.tabs.remove();
        
          // prepare whyShopSlideshow and jQuery cycle tabs
          this.prepareSlideshow();
        }
    },
    
    prepareSlideshow: function() {
        // initialise the jquery cycle plugin -
        // for information on the options set below go to: 
        // http://malsup.com/jquery/cycle/options.html
        $('div.slides > ul', $whyShopSlideshow.context).cycle({
            fx: $whyShopSlideshow.fx,
            timeout: $whyShopSlideshow.timeout,
            speed: $whyShopSlideshow.slideSpeed,
            fastOnEvent: $whyShopSlideshow.tabSpeed,
            pager: $('ul.slides-nav', $whyShopSlideshow.context),
            pagerAnchorBuilder: $whyShopSlideshow.prepareTabs,
            before: $whyShopSlideshow.activateTab,
            pauseOnPagerHover: true,
            pause: true
        });            
    },
    
    prepareTabs: function(i, slide) {
        // return markup from hardcoded tabs for use as jQuery cycle tabs
        // (attaches necessary jQuery cycle events to tabs)
        return $whyShopSlideshow.tabs.eq(i);
    },

    activateTab: function(currentSlide, nextSlide) {
        // get the active tab
        var activeTab = $('a[href="#' + nextSlide.id + '"]', $whyShopSlideshow.context);
        
        // if there is an active tab
        if(activeTab.length) {
            // remove active styling from all other tabs
            $whyShopSlideshow.tabs.removeClass('on');
            
            // add active styling to active button
            activeTab.parent().addClass('on');
        }            
    }            
};


$(function() {
    // add a 'js' class to the body
    $('body').addClass('js');
    
    // initialise the slideshows  when the DOM is ready
    $slideshow.init();
    $tesSlideshow.init();
    $gstSlideshow.init();
    $whyShopSlideshow.init();

});  

