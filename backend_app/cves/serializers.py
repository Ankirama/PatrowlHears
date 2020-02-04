# from django.contrib.auth.models import User
# from django_filters import rest_framework as filters
from django_filters import FilterSet, OrderingFilter
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .models import CVE, CPE, CWE, Bulletin


class CVESerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CVE
        fields = [
            'cve_id', 'summary', 'assigner',
            'published', 'modified',
            'cvss', 'cvss_time', 'cvss_vector',
            'cwe_id', 'access', 'impact', 'vulnerable_products',
            'references', 'bulletins',
            'created_at', 'updated_at'
        ]


class CVEFilter(FilterSet):
    sorted_by = OrderingFilter(
        # tuple-mapping retains order
        choices=(
            ('cve_id', _('CVE-ID')),
            ('-cve_id', _('CVE-ID (desc)')),
            ('cvss', _('CVSSv2')),
            ('-cvss', _('CVSSv2 (desc)')),
            ('modified', _('Modified')),
            ('-modified', _('Modified (desc)')),
        )
    )
    #
    # class Meta:
    #     model = CVE
    #     fields = {
    #         'cve_id': ['icontains'],
    #         'cvss': ['icontains'],
    #     }


class CPESerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CPE
        fields = [
            'title', 'vector',
            'vendor', 'product', 'vulnerable_products'
        ]


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CPE
        fields = ['vendor']


class VendorFilter(FilterSet):
    sorted_by = OrderingFilter(
        # tuple-mapping retains order
        choices=(
            ('vendor', _('Vendor')),
            ('-vendor', _('Vendor (Desc)')),
        )
    )

    class Meta:
        model = CPE
        fields = {
            'vendor': ['icontains']
        }


class ProductFilter(FilterSet):
    sorted_by = OrderingFilter(
        # tuple-mapping retains order
        choices=(
            ('vendor', _('Vendor')),
            ('-vendor', _('Vendor (Desc)')),
            ('product', _('Product')),
            ('-product', _('Product (Desc)')),
        )
    )

    class Meta:
        model = CPE
        fields = {
            # 'vendor': ['icontains'],
            'product': ['icontains'],
        }


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CPE
        fields = ['vendor', 'product', 'title']


class CWESerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CWE
        fields = [
            'cwe_id', 'name', 'description'
        ]


class BulletinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bulletin
        fields = [
            'publicid', 'vendor', 'title', 'severity', 'impact', 'published'
        ]
