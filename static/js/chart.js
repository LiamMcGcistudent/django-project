/*global $*/
/*global Chart*/
/*global console*/
$(document).ready(function () {
    var endpoint = "/graphs/graph_data/";
    var product_labels = [];
    var product_count = [];
    var suggestion_labels = [];
    var suggestion_count = [];
    var upvote_labels = [];
    var upvote_count = [];
    var view_labels = [];
    var view_count = [];
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
            product_labels = data.product_labels;
            product_count = data.product_count;

            suggestion_labels = data.suggestion_labels;
            suggestion_count = data.suggestion_count;

            upvote_labels = data.upvote_labels;
            upvote_count = data.upvote_count;

            view_labels = data.view_labels;
            view_count = data.view_count;

            var suggestionPieChart = $("#suggestionPieChart")[0].getContext("2d");
            suggestionPieChart = new Chart(suggestionPieChart, {
                type: "pie",
                data: {
                    labels: suggestion_labels,
                    datasets: [
                        {
                            data: suggestion_count,
                            backgroundColor: ["#488f31", "#de425b", "#e8979a"]
                        }
                    ]
                },
                options: {
                    legend: {
                        display: true,
                        position: "left",
                        labels: {
                            fontColor: "#f1f1f1",
                            fontSize: 18
                        }
                    }
                }
            });

            var suggestionBarChart = $("#suggestionBarChart")[0].getContext("2d");
            suggestionBarChart = new Chart(suggestionBarChart, {
                type: "bar",
                data: {
                    labels: upvote_labels,
                    datasets: [{
                        label: "# of Votes",
                        data: upvote_count,
                        backgroundColor: [
                            "#488f31",
                            "#f0b8b8",
                            "#83af70",
                            "#e67f83",
                            "#bad0af"
                        ]
                    }]
                },
                options: {
                    legend: {
                        labels: {
                            fontColor: "#f1f1f1"
                        }
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                fontColor: "#f1f1f1"
                            }
                        }],
                        xAxes: [{
                            ticks: {
                                fontColor: "#f1f1f1"
                            }
                        }]
                    }
                }
            });

            var productBarChart = $("#productBarChart")[0].getContext("2d");
            productBarChart = new Chart(productBarChart, {
                type: "bar",
                data: {
                    labels: view_labels,
                    datasets: [{
                        label: "# of Views",
                        data: view_count,
                        backgroundColor: [
                            "#488f31",
                            "#f0b8b8",
                            "#83af70",
                            "#e67f83",
                            "#bad0af"
                        ]
                    }]
                },
                options: {
                    legend: {
                        labels: {
                            fontColor: "#f1f1f1"
                        }
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                fontColor: "#f1f1f1"
                            }
                        }],
                        xAxes: [{
                            ticks: {
                                fontColor: "#f1f1f1"
                            }
                        }]
                    }
                }
            });
        },

        error: function (error_data) {
            console.log("error");
            console.log(error_data);
        }
    });
});