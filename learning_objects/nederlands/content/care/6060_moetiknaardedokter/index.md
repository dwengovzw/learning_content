---
hruid: org-dwengo-moet-ik-naar-de-dokter
version: 1
language: nl
title: "Moet ik naar de dokter?"
description: "De applicatie 'Moet ik naar de dokter' is een regelgebaseerd systeem dat een patient helpt beslissen of en wanneer die de dokter moet contacteren."
keywords: ["beslissingsboom", "zorg", "artificiële intelligentie", "triage"]
content_type: "text/markdown"
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-mediawijsheid',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-digitale-competenties-en-mediawijsheid',
    'http://ilearn.ilabt.imec.be/vocab/onddoel/sec-gr1-astroom-digitale-competenties-en-mediawijsheid-4.5',

]
copyright: "CC BY dwengo"
target_ages: [16, 17, 18]
---


<div id="mindd_widget_embedded" style="height:300px;"></div>

<script src="https://moetiknaardedokter.azurewebsites.net/embed/index.js" type="text/javascript"></script>

<script type="text/javascript">
window.addEventListener('DOMContentLoaded', function() {
	window.mindd.init({
		ApiKey: '0ZJjjXDS6PBNoOfL2opOjOJaRCP2SNUo',
		target: '#mindd_widget_embedded',
		type: 'widget',
		accent_color: '#16B4AD',
		welcome_text: {
			NL: '**Voordat u belt, doorloop eerst deze vragen.** \n\n Wij voorzien u direct van advies', // markdown support
			EN: '**Before you call, first answer our questions.** \n\n We will give you an advice' // markdown support
		},
		open: false,
		modalDisplayMode: 'full', // dialog, full (default)
		widget_showWelcomeText: true,
		widget_background: 'transparent',
		widget_foreground: '#fff',
		showLanguageSelector: true,
		defaultLanguageCode: 'NL',
		getSessionSummaryUsingForm: false,
		startQuestionType: 'gender', // age, gender (default)
		startWithTriageSearch: false,
		startWithAbcdTriage: false,
		labels: {
			QuestionWhatGender: {
				NL: "Bent u geboren als man of vrouw?",
				EN: "Were you born a man or a woman?"
			},
			QuestionWhatSearchTriage: {
				NL: "Van welke gezondheidsklacht heeft u het meeste last?",
				EN: "Which health complaint are you suffering from the most?"
			}
		},
		branding: {
			termsOfUseUrl: "https://www.moetiknaardedokter.nl/gebruikersvoorwaarden/", //(default)
			layout: "top",
			name: "Huisartsenpost MINDD",
			phone_label: "0123 - 456789",
			phone_number: "012356789",
			font_family: "Montserrat"
		},
		onWidgetOpened: function () {
			console.log("Widget was opened; callback");
		},
		onWidgetClosed: (finished) => {
			console.log(`Widget was closed. Was triage finished: ${finished}; callback`);
		},
		onLanguageChanged: function (previousLanguage, newLanguage) {
			console.log(`Language changed from ${previousLanguage.code} to ${newLanguage.code}; callback`);
		}
	});
	
	const el = document.getElementById("mindd_button");
	el.addEventListener("minddWidgetOpened", (e) => {
		console.log("Widget was opened; event");
	});
	el.addEventListener("minddWidgetClosed", (e) => {
		console.log(`Widget was closed. Was triage finished: ${e.detail.finished}; event`);
	});
	el.addEventListener("minddWidgetClosed", (e) => {
		console.log(`Language changed from ${e.detail.previousLanguage.code} to ${e.detail.newLanguage.code}; event`);
	});
});
</script>