import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import datetime, timedelta

class YahooFinanceEarningsResearch:
    """Yahoo Finance 실적공시 및 재무 정보 리서치 도구"""
    
    BASE_URL = "https://finance.yahoo.com"
    
    @staticmethod
    def get_earnings_report(ticker):
        """특정 종목의 실적공시 정보 가져오기"""
        try:
            stock = yf.Ticker(ticker.upper())
            
            # 기본 정보
            info = stock.info
            
            earnings_data = {
                'ticker': ticker.upper(),
                'company_name': info.get('longName', 'N/A'),
                'latest_quarter': info.get('mostRecentQuarter', 'N/A'),
                'earnings_date': info.get('earningsDate', 'N/A'),
                'trailing_eps': info.get('trailingEps', 'N/A'),
                'forward_eps': info.get('forwardEps', 'N/A'),
                'peg_ratio': info.get('pegRatio', 'N/A'),
                'profit_margin': info.get('profitMargins', 'N/A'),
                'operating_margin': info.get('operatingMargins', 'N/A'),
                'revenue': info.get('totalRevenue', 'N/A'),
                'net_income': info.get('netIncomeToCommon', 'N/A'),
                'timestamp': datetime.now().isoformat()
            }
            
            return json.dumps(earnings_data, ensure_ascii=False, indent=2)
        except Exception as e:
            return json.dumps({'error': str(e)}, ensure_ascii=False)
    
    @staticmethod
    def get_quarterly_financials(ticker):
        """분기별 재무제표 정보"""
        try:
            stock = yf.Ticker(ticker.upper())
            
            # 분기별 재무정보
            quarterly_financials = stock.quarterly_financials
            
            financials_summary = {
                'ticker': ticker.upper(),
                'last_updated': datetime.now().isoformat(),
                'quarterly_data': quarterly_financials.to_dict() if quarterly_financials is not None else {}
            }
            
            return json.dumps(financials_summary, ensure_ascii=False, indent=2, default=str)
        except Exception as e:
            return json.dumps({'error': str(e)}, ensure_ascii=False)
    
    @staticmethod
    def get_upcoming_earnings(ticker):
        """예정된 실적공시 날짜"""
        try:
            stock = yf.Ticker(ticker.upper())
            info = stock.info
            
            earnings_info = {
                'ticker': ticker.upper(),
                'company_name': info.get('longName', 'N/A'),
                'earnings_date': info.get('earningsDate', 'N/A'),
                'earnings_avg': info.get('epsTrailingTwelveMonths', 'N/A'),
                'surprise_percent': info.get('epsCurrentYear', 'N/A'),
                'url': f"{YahooFinanceEarningsResearch.BASE_URL}/quote/{ticker.upper()}/analysis",
                'timestamp': datetime.now().isoformat()
            }
            
            return json.dumps(earnings_info, ensure_ascii=False, indent=2)
        except Exception as e:
            return json.dumps({'error': str(e)}, ensure_ascii=False)
    
    @staticmethod
    def get_financial_ratios(ticker):
        """재무비율 정보"""
        try:
            stock = yf.Ticker(ticker.upper())
            info = stock.info
            
            ratios = {
                'ticker': ticker.upper(),
                'pe_ratio': info.get('trailingPE', 'N/A'),
                'forward_pe': info.get('forwardPE', 'N/A'),
                'price_to_book': info.get('priceToBook', 'N/A'),
                'dividend_yield': info.get('dividendYield', 'N/A'),
                'current_ratio': info.get('currentRatio', 'N/A'),
                'quick_ratio': info.get('quickRatio', 'N/A'),
                'debt_to_equity': info.get('debtToEquity', 'N/A'),
                'roe': info.get('returnOnEquity', 'N/A'),
                'roa': info.get('returnOnAssets', 'N/A'),
                'timestamp': datetime.now().isoformat()
            }
            
            return json.dumps(ratios, ensure_ascii=False, indent=2)
        except Exception as e:
            return json.dumps({'error': str(e)}, ensure_ascii=False)
    
    @staticmethod
    def get_analyst_recommendations(ticker):
        """애널리스트 추천 정보"""
        try:
            stock = yf.Ticker(ticker.upper())
            info = stock.info
            
            recommendations = {
                'ticker': ticker.upper(),
                'target_price': info.get('targetMeanPrice', 'N/A'),
                'number_of_analysts': info.get('numberOfAnalysts', 'N/A'),
                'recommendation': info.get('recommendationKey', 'N/A'),
                'recommendation_rating': info.get('recommendationRating', 'N/A'),
                'url': f"{YahooFinanceEarningsResearch.BASE_URL}/quote/{ticker.upper()}/analysis",
                'timestamp': datetime.now().isoformat()
            }
            
            return json.dumps(recommendations, ensure_ascii=False, indent=2)
        except Exception as e:
            return json.dumps({'error': str(e)}, ensure_ascii=False)
    
    @staticmethod
    def search_earnings_calendar(days_ahead=30):
        """예정된 실적공시 캘린더"""
        try:
            # 향후 N일의 예정된 실적공시 정보
            earnings_calendar = {
                'period': f'next_{days_ahead}_days',
                'timestamp': datetime.now().isoformat(),
                'url': f"{YahooFinanceEarningsResearch.BASE_URL}/calendar/earnings",
                'note': 'Use Yahoo Finance earnings calendar for real-time updates'
            }
            
            return json.dumps(earnings_calendar, ensure_ascii=False, indent=2)
        except Exception as e:
            return json.dumps({'error': str(e)}, ensure_ascii=False)
