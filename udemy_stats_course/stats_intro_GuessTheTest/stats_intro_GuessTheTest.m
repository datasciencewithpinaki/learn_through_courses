%%
%   COURSE: Master statistics and machine learning: intuition, math,code										
%      URL: 
% 
%  SECTION: Introduction
%    VIDEO: Statistics guessing game!
% 
%  TEACHER: Mike X Cohen, sincxpress.com
%

%% this section is for parameters that you can specify

% specify the averages of the two groups
average_group1 = 40;
average_group2 = 38;

% the amount of individual variability (same value for both groups)
standard_deviation = .6;

% sample sizes for each group
samples_group1 = 20;
samples_group2 = 35;

%% You don't need to change the code below here!

% Although you are welcome to if you like ;)


%% this section generates the data (don't need to modify)

% generate the data
data_group{1} = randn(samples_group1,1)*standard_deviation + average_group1;
data_group{2} = randn(samples_group2,1)*standard_deviation + average_group2;

% convenient collection of sample sizes
ns = [ samples_group1 samples_group2 ];

%% this section is for data visualization (don't need to modify)

figure(1), clf, hold on

for groupi=1:2
    
    % get histogram counts
    [y,x] = histcounts(data_group{groupi},'BinMethod','fd');
    x = (x(2:end)+x(1:end-1))/2;
    
    % upsample/interpolate to make the plot look nicer
    y = interp1(y,linspace(1,length(y),100),'pchip');
    x = interp1(x,linspace(1,length(x),100),'pchip');
    y = y./max(y);
    
    % draw the actual patch for the violin plot
    patch([y -y(end:-1:1)]+groupi*3 , [x x(end:-1:1)], 'm','facealpha',.5)
    
    % plot all the data points
    plot(groupi*3+randn(ns(groupi),1)/10,data_group{groupi},'ko','markerfacecolor',[.4 .3 .7])
end

% some graphing niceties
set(gca,'xtick',[3 6],'XTickLabel',{'Group 1';'Group 2'})
ylabel('Data values')

%% this section computes the statistics (don't need to modify)

% 2-group t-test
[h,p,c,stats] = ttest2(data_group{1},data_group{2});

% print the information to the title
sigtxt = {' ',' NOT '};
title([ 'The two groups are' sigtxt{(p>.05)+1} 'significantly different! t(' num2str(stats.df) ')=' num2str(round(stats.tstat,3)) ', p=' num2str(round(p,4)) ])

%% done!
