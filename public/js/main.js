(function (window, document, $, _, Backbone, Mustache) {
	
	var ResultModel = Backbone.Model.extend({
		
		defaults: {
			status: 'processing',
			whois: '',
			expanded: false
		},
		
		initialize: function () {
			
			window.app.logView.addResult(this);
			
		},
		
		expand: function () {
			
			this.set('expanded', !this.get('expanded'));
			
			return this.get('expanded');
			
		}
		
	});
	
	var ResultView = Backbone.View.extend({
		
		events: {
			
			'click .expand': 'expand'
			
		},
		
		initialize: function () {
			
			this.listenTo(this.model, 'change', this.render);
			
		},
		
		render: function () {
			
			var query = this.model.get('query'),
				status = this.model.get('status'),
				whois = this.model.get('whois');
			
			this.$el.attr('class', 'result ' + status);
			
			this.$el.html(_.template($('#template-result').html(), {
				query: (status === 'occupied') ? ('<a href="http://' + query + '">' + query + '</a>') : query,
				whois: whois
			}));
			
			return this;
			
		},
		
		expand: function () {
			
			if (this.model.expand()) {
				this.$('.whois').addClass('visible');
			} else {
				this.$('.whois').removeClass('visible');
			}
			
		}
		
	});
	
	var QueryView = Backbone.View.extend({
		
		el: '#query',
		
		events: {
			'click #query-submit': 'submitQuery',
			'keypress #query-input': 'inputQuery'
		},
		
		initialize: function () {
			
			this.$inputEl = this.$('#query-input');
			
		},
		
		submitQuery: function () {
			
			var query = this.$inputEl.val();
			
			if (query) {
				
				var resultModel = new ResultModel({
					query: query
				});
				
				$.ajax({
					url: 'test.json',
					success: function (data) {
						resultModel.set({
							'status': data.status,
							'whois': data.whois
						});
					}
				});
				
			}
			
			this.$inputEl.val('');
			
		},
		
		inputQuery: function (e) {
			
			if (e.keyCode === 13) {
				this.submitQuery();
			}
			
		}
		
	});
	
	var LogView = Backbone.View.extend({
		
		el: '#log',
		
		addResult: function (resultModel) {
			
			var resultView = new ResultView({
				model: resultModel
			});
			
			this.$el.prepend(resultView.render().$el);
			
		}
		
	});
	
	$(function () {
		
		window.app = {};
		
		window.app.queryView = new QueryView();
		
		window.app.logView = new LogView();
		
	});
	
})(this, this.document, this.$, this._, this.Backbone, this.Mustache);
